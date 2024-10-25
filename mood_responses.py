#Defining mood_response function to catch for good alright and bad entries that are received from mood value passed in from main.py
def mood_response(mood):
#Instantiated if statements to respond to specific mood entries and returning response
    if mood.lower() == "good":
        good_response = "Fantastic!"
        return good_response
    if mood.lower() == "alright":
        alright_response = "Better than bad!"
        return alright_response
    if mood.lower() == "bad":
        bad_response = "Hope it gets better!"
        return bad_response
