from screen_functions import printOptions
from common_functions import equal, getValidOption
from symbols import SYMBOLS

def feed(petStats):
	printOptions("FOOD")

	foodChoice = input("Enter food selection: ").upper()

	result = {
		"PIE": 1,
		"PANCAKE": 2,
		"SANDWICH": 4,
		"BROCCOLI": 5,
		"SOUP": 4
	}

	number = result["SANDWICH"]

	try:
		addition = result[foodChoice]

		if (petStats.hunger + addition) >= 10:
			petStats.hunger = 10
		else:
			petStats.hunger = petStats.hunger + addition

		petStats.food_choice = foodChoice
		petStats.status = "EATING"
		petStats.mouth_state = "YUM"
		petStats.eye_state = petStats.getEyeByMood()
	
	except:
		print("That's not food!")

def bathe(petStats):
	petStats.cleanliness = 10
	petStats.coat_state = "CLEAN"



	

