import os # Works with glob to list save file names from the current directory
import glob # works with os to list save file names from the current directory

'''
exp_counter_functions function names:
save_file_list()						- 
print_character_data(character_data)	- 
new_character_data(character_data)	- 
reduce_exp_function(character_data) 	- 
save_data(character_data)				- 
load_data(character_data)				- 
'''

## Prints list of current save files, minus the .txt extension
def save_file_list():
	print("=======================")
	print("CURRENT SAVE FILES ARE:")
	print("-----------------------")
	os.scandir(r'.')
	my_files = glob.glob('*.txt')
	for file in my_files:
		print(file.split(".txt")[0])
	print("=======================")

## Print the contents of the character_data dictionary
def print_character_data(character_data):
	#print("\n")
	print("\n\n===EXP NEEDED TIL NEXT LEVEL===")
	for name, value in character_data.items():
		print(name + ": " + str(value))
	print("===\n\n")

## Create new character data
def new_character_data(character_data):
	character_data.clear()
	print("\n===EXP DATA CREATION MODE===")
	names = input("Please give a character name separated by commas: ").split(', ')
	print("------")
	for name in names:
		character_data[name] = eval(input("Input Remaining EXP Count until {} levels up: ".format(name)))

	print("\n\n===CHARACTER EXP DATA CREATED===")
	return(character_data)

## Reduces character exp by user input amount.
def reduce_exp_function(character_data):
	print("\n===EXP REDUCTION MODE===")
	exp_reduction = eval(input("Please enter a number to reduce exp by: "))

	for name, value in character_data.items():
		character_data[name] -= exp_reduction
		if(character_data[name] < 0):
			print("\n---")
			character_data[name] = eval(input("{} leveled up!\nPlease enter a new exp count for {}:".format(name, name)))
			print("---")
	print("\n\n===EXP Reduce by {} for all characters!===\n\n".format(exp_reduction))
	return(character_data)

## Creates new save data
def save_data(character_data):
	print("\n===SAVE DATA MODE===")
	save_file_list()
	name = input("Please name save file: ")
	name += '.txt'
	with open(name, 'w') as f:
		for name, exp_value in character_data.items():
			f.write("{} : {} \n".format(name, exp_value))

	print("\n\n==CHARACTER DATA SAVED==\n\n")
	return(character_data)

## Loads an existing save data file
def load_data(character_data):
	print("\n===LOAD DATA MODE===")
	character_data.clear()
	save_file_list()
	name = input("Name File You'd Like to Load: ")
	name += '.txt'
	with open(name, 'r') as f:
		for line in f:
			key, val = line.split(':')
			character_data[key] = eval(val)
	print("\n\n==CHARACTER DATA LOADED==\n\n")
	return(character_data)

def main_menu():
	print("MAIN MENU:\n===")
	print("1. Create New Character Data\n2. Print Current Character Data\n3. Reduce Current Character Data's EXP\n4. Save Character Data\n5. Load Character Data\n6. Quit Program")
	print("===")
