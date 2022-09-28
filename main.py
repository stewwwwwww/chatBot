import json
import random_ans
import re
import adventureGame
import wheelOfFortune

# loads jsonfile
def load_json(file):
    with open(file) as responses:
        return json.load(responses)


# store json file
res_data = load_json("answers.json")


def app_response(input_str):
    message_split = re.split(
        r'[~!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?~ ]', input_str.lower())
    score = []

    for res in res_data:
        response_count = 0
        required_count = 0
        # checks if there exists required word(s)
        if len(res["requirement"]) > 0:
            for word in message_split:
                if word in res["requirement"]:
                    required_count += 1
        # checks if requirement for an answer passed
        if len(res["requirement"]) == required_count:
            for word in message_split:
                if word in res["users_input"]:
                    response_count += 1

        score.append(response_count)

        proper_response = max(score)
        res_index = score.index(proper_response)

    if input_str == "":
        return "Please type something so we can chat :("

    if proper_response != 0:
        return res_data[res_index]["app_response"]

    if proper_response == 0:
        return random_ans.random_answers()




def main():
    print("You are chatting with Duc. Ask him anything about himself." + 
    "type 'end' to end the program" + 
    "type 'adventure' to play an adventure game" + 
    "type 'wheel of fortune' to play wheel of fortune")
    username = input("Type your first name: ")
    username = username.capitalize()
    while True:
        users_input = input(username + ": ")
        if users_input.lower() == "end":
            print("It was a nice convo! Thank You!")
            break
        elif users_input.lower() == "adventure":
            adventureGame.adventure()
        elif users_input.lower() == "wheel of fortune":
            wheelOfFortune.wheelOfFortune()
        else:
            print("Duc: " + str(app_response(users_input)))


main()