#Importing custom module with tu as alias
import text_utils as tu

#Creating function for user choice for string mechanisms
def user_interface():
#Creating while loop to ask for user re entry
    while True:
#Using try except block to catch for all other entries
        try:
#Instantiating user choice for operation
            choice = int(input('''What would you like to do?: 
    Menu:
    1. Iterate string by character
    2. Add 'Something' to your string
    3. Turn your string into a list by word
    4. Quit
    
    Please choose any option: '''))
            
#Catches integers outside of range 1-4
            if choice < 1 or choice > 4:
                print("Unable to proceed, choice must be between 1 and 4. Please try again.")
#Sends user choice into custom module using alias, runs defined function in text_utils.py based on entry and returns user to main menu on completion
            elif choice == 1:
                tu.iterate_string()
            elif choice == 2:
                tu.end_string()
            elif choice == 3:
                tu.split_string()
#Loops until option 4 is entered and exits
            elif choice == 4:
                print("Thank you, exiting.")
                exit()
#Using except block to catch for any alpha entries
        except ValueError:
            print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")

#Calling user interface to run
user_interface()