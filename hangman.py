import random

quit = False

while not quit:
    #choose a random word from list
    wordList = ["appel", "banaan", "citroen", "computer", "beeldscherm", "leraar", "student", "behulpzaam", "achterdochtig", "warenhuis", "schietschijf", "directie", "staatsbosbeheer"]
    solution = random.choice(wordList)
    partialSolution = ""
    #fill the partial solution with an amount of dashes equal to the solution length
    for i in solution:
        partialSolution += "_"

    guessList = []
    permittedTries = 10
    #keep asking letters untill the solution is found or we're out of tries
    while permittedTries != 0 and partialSolution != solution:
        #ask for a letter and validate input
        guess = ""
        userInput = input("Kies een letter: ")
        if not userInput.isalpha():
            print("Dit is geeen letter!")
        elif len(userInput) > 1 or len(userInput) == 0:
            print("Voer niet meer of minder dan 1 letter in!")
        #check if the guess is already in guessList (now idea how this works)
        elif any(dict["guess"] == userInput for dict in guessList):
            print("Deze letter heb je al geprobeerd!")
        else:
            guess = userInput
            #check if input is in solution and mark that letter as true or false accordingly
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
        
    if partialSolution == solution:
        print("you win!")  
        quit = True
    else:
        print("you lose!")
        quit = True

