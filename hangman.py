import random
quit = False
def readFile(file):
    wordList = []
    with open(file, "r") as f:
        wordList = [word.rstrip() for word in f]
    return wordList

def randomWord(list):
    return random.choice(list)

def takeGuess(guessList):
    guess = ""
    while guess == "":
        userInput = input("Kies een letter: ")
        if not userInput.isalpha():
            print("Dit is geen letter!")
        elif len(userInput) > 1 or len(userInput) == 0:
            print("Voer niet meer of minder dan 1 letter in!")
        #check if the guess is already in guessList
        elif any(dict["guess"] == userInput for dict in guessList):
            print("Deze letter heb je al geprobeerd!")
        else:
            guess = userInput
    return guess       

def checkSolution(solution, partialSolution):
    if partialSolution == solution:
        print("you win!")  
    else:
        print("you lose!")

def play():
    global quit
    solution = ""
    guessList = []
    wordList = readFile("C:/Users/alber/Documents/hacklab opdrachten/hacklab-documents/Woordlijst.txt")
    solution = randomWord(wordList)
    partialSolution = ""
    permittedTries = 10
    for i in solution:
        partialSolution += "_"
    guessList = []

    while permittedTries != 0 and partialSolution != solution:
        guess = takeGuess(guessList)
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
    checkSolution(solution, partialSolution)
    rematch = ""
    while rematch != "y" and rematch != "n":
        rematch = input("Rematch? \"y\" or \"n\"")
    if rematch == "n":
        quit = True

while not quit:
    play()