sequence = "CGATTGCGTATAAGCACCAA"
complementaireSequence = ""

#dna sequence altijd c + g, a + t en vise versa
'''for i in sequence:
    if i == "C":
        complementaireSequence += "G"
    elif i == "G":
        complementaireSequence += "C"
    elif i == "A":
        complementaireSequence += "T"
    elif i == "T":
        complementaireSequence += "A"

print("originele sequence:      " + sequence)
print("complementaire sequence: " + complementaireSequence)'''

#dna strikes back
sequence = "CGATTGCGTATAAGCACCAA"
dnaDict = {"C":"G","G":"C","A":"T","T":"A"}
compSequence = ""
print(compSequence.join([dnaDict[x] for x in sequence]))

