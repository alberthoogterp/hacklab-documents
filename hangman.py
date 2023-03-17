import random

quit = False

def readFile(file):
    wordList = []
    with open(file, "r") as f:
        wordList = [word.rstrip() for word in f]
    return wordList

def randomWord(list):
    return random.choice(list)

def takeGuess(guess, guessList):
    if not guess.isalpha():
        print("Dit is geen letter!")
    elif len(guess) > 1 or len(guess) == 0:
        print("Voer niet meer of minder dan 1 letter in!")
    #check if the guess is already in guessList
    elif any(dict["guess"] == guess for dict in guessList):
        print("Deze letter heb je al geprobeerd!")
    else:
        return guess       

def checkGuess(guess, solution, guessList, permittedTries, partialSolution):
    if guess in solution:
        guessList.append({"guess":guess, "inSolution":True})
        #fill in blanks on partialsolution
        tempPartialSolution = ""
        for i in range(len(partialSolution)):
            if partialSolution[i] == "_" and solution[i] == guess:
                tempPartialSolution += guess
            else:
                tempPartialSolution += partialSolution[i]
        partialSolution = tempPartialSolution
    else:
        guessList.append({"guess":guess, "inSolution":False})
        permittedTries -= 1
        print(partialSolution)
        print("Je hebt nog " + str(permittedTries) + " beurten over")

def checkSolution(solution, partialSolution):
    if partialSolution == solution:
        print("you win!")  
        quit = True
    else:
        print("you lose!")
        quit = True
    
def play():
    solution = ""
    guessList = []
    wordList = readFile("Woordlijst.txt")
    solution = randomWord(wordList)
    partialSolution = ""
    for i in solution:
        partialSolution += "_"
    guessList = []
    permittedTries = 10

    while permittedTries != 0 and partialSolution != solution:
        userInput = input("Kies een letter: ")
        guess = takeGuess(userInput, guessList)
        checkGuess(guess, solution, guessList, permittedTries, partialSolution)
    checkSolution(solution, partialSolution)
    rematch = ""
    while rematch != "y" or rematch != "n":
        rematch = input("Rematch? \"y\" or \"n\"")
    if rematch == "n":
        quit = True

while not quit:
    play()