import random

dnaList = ["A", "C", "G", "T"]

def createSequence(seqRange, list):
    randomSequence = ""
    for i in range(seqRange):
        randomLetter = random.choice(list)
        randomSequence += randomLetter
    return randomSequence

def createComplement(sequence):
    compSequence = ""
    for i in sequence:
        if i == "A":
            compSequence += ("T")
        elif i == "C":
            compSequence += ("G")
        elif i == "G":
            compSequence += ("C")
        elif i == "T":
            compSequence += ("A")
    return compSequence

print(createComplement(createSequence(10, dnaList)))
