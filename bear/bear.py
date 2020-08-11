x, y = map(int, input().split());
year =0;

while x<=y:
        x*=3
        y*=2
        year+=1
        
print(year)
