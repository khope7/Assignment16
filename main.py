#Importing custom module with mood responses
import mood_responses

#Creating loop to ask user for mood and sends user to mood_responses.py and runs define function based on user choice. Using break to exit run after any entry
while True:
#Defining accepted entries and rejecting all other entries
    mood = input("How are you feeling today? please type one of the following: (good/alright/bad): ")
#Using .lower() method to ignore user case
    if mood.lower() == "good" or mood.lower() == "alright" or mood.lower() == "bad":
#Printing mood response from defined function in mood_responses.py, breaking to exit run after user entry
        print(mood_responses.mood_response(mood))
        break
#Catching all other entries and asking for user re entry
    else:
        print("Apologies, entry must be one of the above mentioned (good/alright/bad). Please try again.")