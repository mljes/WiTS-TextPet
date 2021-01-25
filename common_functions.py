from symbols import SYMBOLS
from colors import FG_COL, BG_COL, RESET

def equal(actual, expected):
	return actual.upper().rstrip() == expected.upper()

def getSymbols(section, item):
	print(SYMBOLS[section][item])

def getValidOption(string, source):
	try:
		result = source[string.upper()].upper()
	except:
		result = "NONE"
	finally:
		print(result)
		return string

def getValidAddition(item, source):
	try:
		result = source[item.upper()]
	except:
		print("That wasn't an option!")
		result = 0
	finally: 
		return result

		




