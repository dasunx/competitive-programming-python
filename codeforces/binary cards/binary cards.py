x = int(input())
arr = input()
res = []

for i in range(x):
    if(arr[i] == "n"):
        res.append(1)
    if(arr[i] == "z"):
        res.append(0)

res.sort(reverse=True)
print(*res, sep = " ")
