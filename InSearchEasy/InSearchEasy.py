x = int(input())
arr = list(map(int, input().split()))
h = 0;

for i in range (x):
    if(arr[i] == 1):
        h=1;
        break;

if h==1:
    print("Hard")
else:
    print("easy")
