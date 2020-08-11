x = int(input())
y=[]
for i in range(x):
    y.append(input())

for i in range(x):
    s = y[i]
    if(s.endswith("po")):
        print("FILIPINO")
    elif(s.endswith(("desu","masu"))):
        print("JAPANESE")
    else:
        print("KOREAN")
