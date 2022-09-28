"""
This program execute a game called Adventure game which is
text-based where player select choices and the game will
run base on those choices.

Answer:
Math Room: 98
Sport Room: "Lacrosse" or "lacrosse"
Physics Room: 9,8 or 9.8
Geo Room: 50
Biology Room: "dog" or "Dog"
Chemistry Room: "water" or "Water"

"""

import random


def luck():
    repeat = True # set repeat = True to repeat in case user input invalid value
    luckyNumber = random.randint(1, 10) #declare number (number is a number from 1 to 10)
    print("Please input a lucky number to pass the room: ") #ask user to pick a number
    while repeat:
        pickNum = int(input("Your lucky number: ")) #user pick correct lucky number
        if pickNum == luckyNumber: #user pick correct lucky number
            print("You have picked the lucky number")
            repeat = False
        elif pickNum > luckyNumber: #number user picked is larger than the luck number
            print(
                "You have picked a number that is larger than the lucky number. Try again")
        else: #number user picked is smaler than the luck number
            print(
                "You have picked a number that is smaller than the lucky number. Try again")


def mathRoom():
    """
    This function informs that the user has entered Math Room, then
    ask the Math question(ask again if input is valid). If user 
    answer correctly, it will ask the user to move to the next room
    (user's choice)
    Parameters:  None
    Return: None
    """

    print("You have enter Math Room!")  # inform user
    print("A question appears and you have to answer it if you\n want to leave the room.\n The question is: 14 + 84 = ?")  # inform user

    repeat = True  # set repeat = True to repeat in case user input invalid value

    while repeat:  # repeat in case user input invalid value
        answer = input("type you answer: ")  # get answer from user
        answer = answer.strip()
        if answer == "98":  # check if answer is correct
            # inform user
            print("You have answer the correct answer\n2 doors that lead to Physics Room and Geo Room appear\nWhich room would you like to enter?")

            while repeat:  # repeat in case user input invalid value
                # ask user which room they want to go
                enterRoom = input(
                    "Enter '3' for Physics Room or '4' for GeoRoom or 'Q' to get out: ")
                enterRoom = enterRoom.strip()
                if enterRoom == "3":  # enter room 3
                    physicsRoom()
                    repeat = False  # change the value of repeat to stop the loop
                elif enterRoom == "4":  # enter room 4
                    geoRoom()
                    repeat = False  # change the value of repeat to stop the loop
                elif enterRoom == "Q" or enterRoom == "q":  # quit the building
                    print("You got out of the building! Thanks for playing")
                    repeat = False  # change the value of repeat to stop the loop

                else:
                    # inform user to try again
                    print("you have enter an invalid room, try again.")

        else:
            print("You have entered an incorrect answer, try again.")


def sportRoom():
    """
    This function informs that the user has entered Sport Room, then
    ask the Sport question(ask again if input is valid). If user 
    answer correctly, it will ask the user to move to the next room
    (user's choice)
    Parameters:  None
    Return: None
    """

    print("You have enter Sport Room!")  # inform user
    print("A question appears and you have to answer it if you\nwant to leave the room.\nThe question is: What is the national sport of Canada?")  # inform user

    repeat = True  # set repeat = True to repeat in case user input invalid value

    while repeat:  # repeat in case user input invalid value
        answer = input("type you answer: ")  # get answer from user
        answer = answer.lower().strip()
        if answer == "lacrosse":  # check if answer is correct
            # inform user
            print("You have answer the correct answer\n2 doors that lead to Biology Room and Chemistry Room appear\nWhich room would you like to enter?")

            while repeat:  # repeat in case user input invalid value
                # ask user which room they want to go
                enterRoom = input(
                    "Enter '5' for Biology Room or '6' for Chemistry Room or 'Q' to get out: ")
                enterRoom = enterRoom.strip()
                if enterRoom == "5":  # enter room 5
                    bioRoom()
                    repeat = False  # change the value of repeat to stop the loop
                elif enterRoom == "6":  # enter room  6
                    chemRoom()
                    repeat = False  # change the value of repeat to stop the loop
                elif enterRoom == "Q" or enterRoom == "q":  # quit the building
                    print("You got out of the building! Thanks for playing")
                    repeat = False  # change the value of repeat to stop the loop

                else:
                    # inform user to try again
                    print("you have enter an invalid room, try again.")

        else:
            print("You have entered an incorrect answer, try again.")


def physicsRoom():
    """
    This function informs that the user has entered Physics Room, then
    ask the Physics question(ask again if input is valid). If user 
    answer correctly, it will inform that this is the end of the
    game
    Parameters:  None
    Return: None
    """

    print("You have enter Physics Room!")  # inform user
    print("A question appears and you have to answer it if you\nwant to leave the room.\nThe question is: What is the value of gravity on earth (1 decimal place)?")  # inform user

    repeat = True  # set repeat = True to repeat in case user input invalid value

    while repeat:  # repeat in case user input invalid value
        answer = input("type you answer: ")
        answer = answer.strip()
        if answer == "9,8" or answer == "9.8":  # check if answer if correct
            print("You have answer the correct answer")
            print(
                "A treasure appear. Pick the correct lucky number to open the treasure!")
            luck()
            # inform user
            print("Congratulations! You cannot go any\nfurther. Thanks for playing")
            repeat = False  # change the value of repeat to stop the loop

        else:
            # inform user to retry
            print("You have entered an incorrect answer, try again.")


def geoRoom():
    """
    This function informs that the user has entered Geo Room, then
    ask the Geo question(ask again if input is valid). If user 
    answer correctly, it will inform that this is the end of the
    game
    Parameters:  None
    Return: None
    """

    print("You have enter Geo Room!")  # inform user
    print("A question appears and you have to answer it if you\nwant to leave the room.\nThe question is: How many states are there in the United States?")  # inform user

    repeat = True  # set repeat = True to repeat in case user input invalid value

    while repeat == True:  # repeat in case user input invalid value
        answer = input("type you answer: ")
        answer = answer.strip()
        if answer == "50":  # check if answer if correct
            print("You have answer the correct answer")
            print(
                "A treasure appear. Pick the correct lucky number to open the treasure!")
            luck()
            # inform user
            print("Congratulations! You cannot go any\nfurther. Thanks for playing")
            repeat = False  # change the value of repeat to stop the loop

        else:
            # inform user to retry
            print("You have entered an incorrect answer, try again.")


def bioRoom():
    """
    This function informs that the user has entered Biology Room, then
    ask the Biology question(ask again if input is valid). If user 
    answer correctly, it will inform that this is the end of the
    game
    Parameters:  None
    Return: None
    """

    print("You have enter Biology Room!")  # inform user
    print("A question appears and you have to answer it if you\nwant to leave the room.\nThe question is: What animal hates cats?")  # inform user

    repeat = True  # set repeat = True to repeat in case user input invalid value

    while repeat == True:  # repeat in case user input invalid value
        answer = input("type you answer: ")
        answer = answer.lower().strip()
        if answer == "dog" or answer == "Dog":  # check if answer if correct
            print("You have answer the correct answer")
            print(
                "A treasure appear. Pick the correct lucky number to open the treasure!")
            luck()
            # inform user
            print("Congratulations! You cannot go any\nfurther. Thanks for playing")
            repeat = False  # change the value of repeat to stop the loop

        else:
            # inform user to retry
            print("You have entered an incorrect answer, try again.")


def chemRoom():
    """
    This function informs that the user has entered Chemistry Room, then
    ask the Chemistry question(ask again if input is valid). If user 
    answer correctly, it will inform that this is the end of the
    game
    Parameters:  None
    Return: None
    """

    print("You have enter Chemistry Room!")  # inform user
    print("A question appears and you have to answer it if you\nwant to leave the room.\nThe question is: What is H2O?")  # inform user

    repeat = True  # set repeat = True to repeat in case user input invalid value

    while repeat == True:  # repeat in case user input invalid value
        answer = input("type you answer: ")
        answer = answer.lower().strip()
        if answer == "water" or answer == "Water":  # check if answer if correct
            print("You have answer the correct answer")
            print(
                "A treasure appear. Pick the correct lucky number to open the treasure!")
            luck()
            # inform user
            print("Congratulations! You cannot go any\nfurther. Thanks for playing")
            repeat = False  # change the value of repeat to stop the loop

        else:
            # inform user to retry
            print("You have entered an incorrect answer, try again.")


def adventure():
    """
    This is the main function which executes the program

    Parameters: None
    Return: None
    """

    # inform that user has entered the building
    print("You entered Trivia Building. There is a treasure in this building. There are 2 doors that lead to\nMath Room and Sport Room. Which room would you like to enter?")

    repeat = True  # set repeat = True to repeat in case user input invalid value

    while repeat == True:  # repeat in case user input invalid value
        enterRoom = input("Enter '1' for Math Room or '2' for Sport Room: ")
        if enterRoom == "1":  # if user chooses math room
            mathRoom()
            repeat = False  # stop the loop
        elif enterRoom == "2":  # if user chooses sport room
            sportRoom()
            repeat = False  # stop the loop
        else:
            # inform that user entered invalid room and ask them to try again
            print("you have enter an invalid room, try again.")


