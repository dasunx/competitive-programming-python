x = int(input())
count=0

for i in range(int(x/2)):
    j= ((x-(i+1))%(i+1))
    if(j == 0):
        count+=1
print(count)
        
