from symbols import SYMBOLS
from colors import FG_COL, BG_COL, RESET

#############################################
# SCREEN FIELDS
max_width = 44
max_height = 13
#############################################

def printOptions(type):
	printFrame("TOP", max_width-2)

	for item in SYMBOLS[type]:
		if item != "NONE":
			option = SYMBOLS["LINE"]["V"] + SYMBOLS[type][item] +  "  " + item
			
			if len(SYMBOLS[type][item]) < 10:
				opt_size = len(option) + 1
			else:
				opt_size = len(option)
			
			print(option, end="")

			for i in range(max_width - opt_size + 8):
				print(" ", end="")

			print(SYMBOLS["LINE"]["V"])

	printFrame("BOTTOM", max_width-2)

def printFrame(top_bottom, width):
	top_bottom = top_bottom.upper()

	print(SYMBOLS["CORNER"][top_bottom + "_LEFT"], end="")
	print(SYMBOLS["LINE"]["H"] * (width), end="")
	print(SYMBOLS["CORNER"][top_bottom + "_RIGHT"])

def setForeColor(color, text):
	return FG_COL[color] + text + RESET

def setBackColor(color, text):
	return BG_COL[color.upper()] + text + RESET

def clearScreen():
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')