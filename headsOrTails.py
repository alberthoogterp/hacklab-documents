import random

def headsOrTails(times):
    headCount = 0
    for i in range(times):
        coin = random.choice(["heads","tails"])
        if coin == "heads":
            headCount += 1
    print("we flipped the coin "+ str(times) +" times, it was heads "+str(headCount)+" times, and tails "+ str(times - headCount)+" times")
headsOrTails(10)