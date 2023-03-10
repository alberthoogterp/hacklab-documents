arrowWidth = ""

while not arrowWidth.isnumeric():
    arrowWidth = input("Hoe breed moet de @ arrow worden? ")

arrowWidth = int(arrowWidth)
length = arrowWidth * 2

for i in range(1, length):
    if(i > arrowWidth):
        print((length - i) * "@")
    else:
        print(i * "@")