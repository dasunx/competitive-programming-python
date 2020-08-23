x = input()

countA = x.count("a")
countOther = len(x)-countA

if(countOther>=countA):
    print(countA + (countA-1))
else:
    print(countA + countOther)
