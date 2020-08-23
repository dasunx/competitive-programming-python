x = input()
y = list(input().split())
v = "no"
for i in range(5):
    if(x[0] == y[i][0] or x[1] == y[i][1]):
        v = "yes"
        break
    
print(v)
