from common_functions import equal, getSymbols
from game_functions import feed, bathe
from new_functions import changeHat, play
from screen_functions import clearScreen
from pet_stats import PetStats

response = input("Enter pet name: ")

petName = response
petStats = PetStats(petName)

while not equal(response, "exit"):
	clearScreen()
	petStats.printStats()

	response = input("What do you want to do? ")
	print("You said: " + response)

	if equal(response, "feed"):
		feed(petStats)

		petStats.printStats()

		input("[Press Enter to continue]")

		petStats.decreaseBoredom(1)
		petStats.decreaseCleanliness(1)
		petStats.resetObjects()
		

	elif equal(response, "play"):
		play(petStats)

		petStats.printStats()

		input("[Press Enter to continue]")

		petStats.decreaseHunger(1)
		petStats.decreaseCleanliness(1)
		petStats.resetObjects()

	elif equal(response, "clean") or equal(response, "bathe"):
		bathe(petStats)

		petStats.decreaseHunger(1)
		petStats.decreaseBoredom(1)
		petStats.resetObjects()

	elif equal(response, "dress"):
		changeHat(petStats)

		petStats.decreaseHunger(1)
		petStats.decreaseBoredom(1)
		petStats.decreaseCleanliness(1)
		petStats.resetObjects()

	elif equal(response, "get"):
		section = input("section: ")
		item = input("item: ")
		getSymbols(section.upper(), item.upper())

	elif equal(response, "quit"):
		break
	else:
		print("\nHere are your options: ")
		print("clean -- restore CLEANLINESS stat")
		print("play  -- improve BOREDOM stat")
		print("feed  -- improve HUNGER stat")
		print("dress -- change your pet's hat")
		print("quit  -- exit game")
		input("\n[Press Enter to continue]")

print("Bye for now!")