import exp_counter_functions
import os
'''
exp_counter_functions function names:
save_file_list()						- Prints list of current save files, minus the .txt extension
print_character_data(character_data)	- Print the contents of the character_data dictionary
new_character_data(character_data)		- Create new character data
reduce_exp_function(character_data) 	- Reduces character exp by user input amount.
save_data(character_data)				- Creates new save data
load_data(character_data)				- Loads an existing save data file
main_menu()								- Prints the main menu
'''

#Global Variables
character_data = dict()


os.chdir('save_data') #changes working directory to save_data subfolder. DO NOT DELETE

def main():
	option = 0
	print("\n\n====================")
	while option != 6:
		exp_counter_functions.main_menu()
		option = eval(input("Which Option Would You Like to do: "))
		print("===")
		# 1. Create New Character Data
		if option == 1:
			exp_counter_functions.new_character_data(character_data)
		# 2. Print Current Character Data
		elif option == 2:
			exp_counter_functions.print_character_data(character_data)
		# 3. Reduce Current Character Data's EXP
		elif option == 3:
			exp_counter_functions.reduce_exp_function(character_data)
		# 4. Save Character Data
		elif option == 4:
			exp_counter_functions.save_data(character_data)
		# 5. Load Character Data
		elif option == 5:
			exp_counter_functions.load_data(character_data)
		# 6. Quit Program
		# If not a valid option do the following
		elif option >= 7 or option < 0:
			print("INVALID OPTION")
		print("=============")

	print("PROGRAM END")

main()



