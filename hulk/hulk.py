x = int(input())
out ="";

for i in range (x):
    if((i+1)%2 ==1):
        out = "".join((out,"I hate "))
    else:
        out = "".join((out,"I love "))
    if((i+2)<=x):
       out = "".join((out,"that "))

print(out+"it")
