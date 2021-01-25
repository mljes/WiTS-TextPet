from screen_functions import setForeColor, setBackColor
import random
from colors import VIOLET, RESET, RED
from symbols import SYMBOLS

class PetStats:
	def __init__(self, name):
		self.name = name
		self.boredom = random.randint(1, 10)
		self.hunger = random.randint(1, 10)
		self.boredom = random.randint(1, 10)
		self.cleanliness = random.randint(1, 10)

		self.status = "IDLE"
		
		self.coat_state = self.getCoatByCleanliness() #or dirty
		self.mouth_state = self.getMouthByMood()
		self.eye_state = self.getEyeByMood()
		self.hat_choice = "CROWN" #or NONE
		self.toy_choice = "NONE"
		self.food_choice = "NONE"
	
	imageArr = [
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
		["0","0","0","0","0","4","3","5","3","4","0","0","0","0","0"],
		["0","0","0","0","6","D","8","9","8","D","7","0","0","0","0"],
		["0","0","0","0","0","1","D","D","D","2","0","0","0","0","0"],
		["0","0","0","E","0","B","A","0","A","C","0","F","0","0","0"],
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
		["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
	]
	
	def getTextStat(self, stat):
		return stat + (" " * (11-(len(stat))))
		
	def getBarStat(self, stat):
		result = (" " * stat)

		if (stat >= 8):
			result = setBackColor("CYAN", result) 
		elif (stat >= 6):
			result = setBackColor("GREEN", result)
		elif (stat >= 4): 
			result = setBackColor("YELLOW", result)
		else:
			result = setBackColor("RED", result)

		if (stat < 10):
			result = result + (" " * (10-stat))
		
		return result

	def renderPetImage(self):
		MAPPINGS = {
			"1": VIOLET + "(" + RESET,
			"2": VIOLET + ")" + RESET,
			"3": VIOLET + "_" + RESET,
			"4": VIOLET + SYMBOLS["EAR"]["TOP_TRIANGLE"] + RESET,
			"5": SYMBOLS["HAT"][self.hat_choice],
			"6": SYMBOLS["WHISKERS"]["LEFT"],
			"7": SYMBOLS["WHISKERS"]["RIGHT"],
			"8": SYMBOLS["EYE"][self.eye_state], 
			"9": RED + SYMBOLS["MOUTH"][self.mouth_state] + RESET,
			"0": " ",
			"A": VIOLET + SYMBOLS["FOOT"]["CENTER"] + RESET,
			"B": VIOLET + SYMBOLS["FOOT"]["LEFT"] + RESET,
			"C": VIOLET + SYMBOLS["FOOT"]["RIGHT"] + RESET,
			"D": SYMBOLS["COAT"][self.coat_state],
			"E": SYMBOLS["TOY"][self.toy_choice],
			"F": SYMBOLS["FOOD"][self.food_choice]
		}

		renderedArr = []

		for row in self.imageArr:
			imageStr = ""
			for col in row:
				imageStr = imageStr + MAPPINGS[col]

			renderedArr.append(imageStr)

		return renderedArr

	############################################################
	# set face and body features based on mood stats
	############################################################
	def getMouthByMood(self):
		if self.boredom < 5 or self.hunger < 5:
			return "FROWN"
		else:
			return "SMILE"

	def getEyeByMood(self):
		if self.boredom < 3 and self.hunger < 3:
			return "ANGRY"
		else:
			return "NORMAL"

	def getCoatByCleanliness(self):
		if self.cleanliness < 4:
			return "DIRTY"
		else:
			return "CLEAN"
		
	def resetObjects(self):
		self.food_choice = "NONE"
		self.toy_choice = "NONE"
		self.eye_state = self.getEyeByMood()
		self.mouth_state = self.getMouthByMood()
		self.coat_state = self.getCoatByCleanliness()
		self.status = "IDLE"
	
	############################################################
	# Decrease stats
	############################################################
	def decreaseHunger(self, amt):
		if self.hunger != 1:
			self.hunger = self.hunger - amt

	def decreaseBoredom(self, amt):
		if self.boredom != 1:
			self.boredom = self.boredom - amt

	def decreaseCleanliness(self, amt):
		if self.cleanliness != 1:
			self.cleanliness = self.cleanliness - amt

	def increaseHunger(self, amt):
		if self.hunger + amt >= 10:
			self.hunger = 10
		else:
			self.hunger = self.hunger + amt
	
	def increaseCleanliness(self, amt):
		if self.cleanliness + amt >= 10:
			self.cleanliness = 10
		else:
			self.cleanliness = self.cleanliness + amt

	def increaseBoredom(self, amt):
		if self.boredom + amt >= 10:
			self.boredom = 10
		else:
			self.boredom = self.boredom + amt

	############################################################
	# Print stats and pet
	############################################################
	def printStats(self):
		
		pet = self.renderPetImage()

		print("┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
		print("┃" + pet[0] + "┃ NAME:         " + self.getTextStat(self.name) + "┃") 
		print("┃" + pet[1] + "┃                          ┃")    
		print("┃" + pet[2] + "┃ BOREDOM:      " + self.getBarStat(self.boredom) + " ┃")        
		print("┃" + pet[3] + "┃                          ┃")         
		print("┃" + pet[4] + "┃ HUNGER:       " + self.getBarStat(self.hunger) + " ┃")        
		print("┃" + pet[5] + "┃                          ┃")         
		print("┃" + pet[6] + "┃ CLEANLINESS:  " + self.getBarStat(self.cleanliness) + " ┃") 
		print("┃" + pet[7] + "┃                          ┃")         
		print("┃" + pet[8] + "┃ STATUS:       " + self.getTextStat(self.status) + "┃")      
		print("┗━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━┛")