x = int(input())
arr=[];
d = 0;
y = 0;
for i in range (x):
    arr.append(list(input().split()))


for i in range(x):
    for j in range(3):
        if(arr[i][j] == "1"):
            d+=1;
    if(d>=2):
        y+=1
    d=0;

print(y)
