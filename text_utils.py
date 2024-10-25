#Defining iterate_string to add a space to the end of every character
def iterate_string():
#Using user_string to take in user imput for each function
    user_string = input("What would you like to say?: ")
    print(f"Iterating String:")
    for char in user_string:
        print(char, end = " ")
#Using print to create new line for main menu print
    print("")

#Defining end_string to add +Something to every string
def end_string():
    user_string = input("What would you like to say?: ")
    print(f"Adding Something to String:")
    print(user_string, end = " +Something\n")

#Defining split_string to create a list of elements from string of user entry based on spaces
def split_string():
    user_string = input("What would you like to say?: ")
    print(f"Spliting String into list based on spaces:")
    element = user_string.split(" ")
    print(element)