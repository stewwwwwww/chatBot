'''
This implements a simplified version of Wheel of Fortune. The computer chooses a word
from a list of words and the user guesses letters until they have filled in all the letters 
in the word or have guessed incorrectly 5 times.
'''
import random

def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the word
    """

    validWords = ["queens", "science", "brock", "java", "cyberpunk", "edgerunners", "toronto", "cisc"]

    

    return validWords[random.randint(0,len(validWords) - 1)]

def printStringWithSpaces(word):
    """
    This function prints the word representation (eg: "__r_")
    on the screen with spaces between each underscore/letter
    so that the user can better see how many letters there are.
    Parameter: string
    Return Value:  None
    """

    for i in range(len(word)):
        print(word[i], end=" " ) #print the word with sapce in between each letter

    print()
    print()


def convertToUnderscores(word):
    """
    Creates a string consisting of len(word) underscores.
    For example, if word = "cat", function returns "___" (3 underscores)

    Parameter: string
    Return Value: string
    """

    underscore = "" 

    for i in range(len(word)):
        underscore += "_" #add underscore for each letter of the word
    return underscore

    

def updateWord(currentRep, word, letter):
    """
    This function replaces the underscores with the guessed letter.
    Eg.  letter = 'p', word = "stop", currentRep = "s___" --> returns "s__p"
    Paramters:   currentRep, word are strings
                letter is a string, but a single letter.
    Returns:  a string
    """

    newString = ""
    for i in range(len(word)):
        if letter == word[i]:
            newString += letter #add letter if the guess is correct
        else:
            newString += currentRep[i] #add an underscore if the word is incorrect
    return newString
        

    
def updateUsedLetters(usedLetters, letter):
    """
    This function concatenates the guessed letter onto the list of letters
    that have been guessed, returning the result.
    Parameters: string representing the used letters
                string respresenting the current user guess
    Return Value:  string
    """

    usedLetters += letter #add letter the the used letters list
    return usedLetters
    

    

def wheelOfFortune():
    """
    This implements the user interface for the program.
    """
    usedLetters = "" #no letters guessed yet
    wrongGuesses = 0 #keep track of incorrect guesses

    #the word to guess
    word = chooseWord()

    print("The word to guess is ", word)  

    
    currentRep = convertToUnderscores(word)   #convert the word to underscore


    print(convertToUnderscores(word))

    #continueGame is a flag that will turn to false when the user wins or loses
    #the game.
    continueGame = True
    while continueGame:
        guess = input("Please enter a letter (a-z): ") #ask user for a guess
        
        #check for valid input
        while not(guess.isalpha()) or len(guess) != 1:
            guess = input("Please enter valid input(a single letter (a-z)):") #ask user for a guess if the previous input was invalid
            
        guess = guess.lower() #make the letter lower so capital input can be valid

        print("You have guessed ", guess)

        if guess not in usedLetters:
            updateUsedLetters(usedLetters, guess) #update used letters list
            if guess in word:
                #letter is in the secret word so update the current representation
                currentRep = updateWord(currentRep, word, guess) #update the current word
                printStringWithSpaces(currentRep) #print out the current word
                if word ==  currentRep:
                    print("Congratulations! you won") #inform that they won
                    continueGame = False #stop the game

            else:
                wrongGuesses += 1 #increase number of wrong guesses
                if wrongGuesses == 5:
                    print("The letter is not in the word!")
                    print("Sorry! you lost. Better luck next time!") #inform that they lost
                    continueGame = False #stop the game           
        else:
            #letter has been guessed already -- update the user
            print("You have already guessed that letter!!!")
            print("Here are the letters you have guessed so far: ") # inform that letter has been guessed
            printStringWithSpaces(usedLetters)
            


