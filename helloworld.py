'''print("Hello world")'''

'''uren = 5
minuten = uren * 60
seconden = minuten * 60
print("uren:"+str(uren) +" minuten:"+str(minuten)+" seconden:"+str(seconden) )'''

'''tafel = int(input("voer tafel in:"))
#print(f"1 * {tafel} = {1 * tafel} 2 * {tafel} = {2 * tafel} 3 * {tafel} = {3 * tafel} 4 * {tafel} = {4 * tafel}")
for x in range(1,11):
    print(str(tafel) + " * " + str(x) + " = " + str(tafel * x))'''

'''getal = int(input("geef getal "))
if getal > 10:
    print("groter dan 10")
elif getal < 10:
    print("kleiner dan 10")
elif getal == 10:
    print("gelijk aan 10")
else:
    print("geen getal")'''

'''input = int(input("geef getal: "))
print("de tafel van " + str(input) + " =")
for i in range(1, 11):
    print(i * input)'''

'''for i in range(1,101):
    text = ""
    if(i % 5 == 0):
        text += "fizz"
    if(i % 7 == 0):
        text += "buzz"
    print(str(i) + " " + text)'''


'''concatstring = ""
lijst_namen = ["albert", "juwell", "gerlof-Jan", "martin", "aina", "danny", "karsten"]
for i in lijst_namen:
    print(f"{i}")
    concatstring += i
print(concatstring)
print("{}".format(concatstring))'''

'''lijstvanrandomdingen = ["scania", "belgie", "albert", 46]
dict = {}
dict.update({"auto":lijstvanrandomdingen[0]})
dict.update({"land":lijstvanrandomdingen[1]})
dict["naam"] = lijstvanrandomdingen[2]
dict["nummer"] = lijstvanrandomdingen[3]
print(dict)'''

'''test = "xooxxoo"

def evenChecker(string):
    oCount = 0
    xCount = 0

    for i in string:
        if i == "o":
            oCount += 1
        if i == "x":
            xCount += 1

    return oCount == xCount

print(evenChecker(test))'''

'''testString1 = "albert"
testString2 = "arbattjoihjv"

def hammingDistance(string1, string2):
    diff = 0
    longestString = string1 if len(string1) > len(string2) else string2
    for i in range(len(longestString)):
        try: 
            if string1[i] != string2[i]:
                diff += 1
        except:
            diff += 1

    return diff

print(hammingDistance(testString1,testString2))'''

'''def difCheck(start, stop, divider):
    try:
        return [i for i in range(start,stop+1) if i % divider == 0]
    except: 
        return []
print(difCheck(1, 10, 2))'''

'''def repeat(string):
    return "".join([i*2 for i in string])

print(repeat("hall23 o"))'''

