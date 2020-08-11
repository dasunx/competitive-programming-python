x, y = map(int, input().split());
for i in range(y):
    if(x%10 == 0):
        x/=10
    else:
        x-=1;

s = int(x)
print(s)
