n=input()

zero = n.split("0")
one = n.split("1")
changeZero = 0  
changeOne = 0

for i in zero:
    if i != "":
        changeZero += 1

for i in one:
    if i != "":
        changeOne += 1

if changeZero<changeOne:
    print(changeZero)
else:
    print(changeOne)
