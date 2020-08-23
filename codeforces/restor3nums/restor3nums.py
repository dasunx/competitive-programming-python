x = list(map(int, input().split()))
maxc = (max(x))
minc =(min(x))
t = maxc-minc
x.remove(max(x))
x.remove(min(x))
a = x[0]- t
b = x[1] - t

print(t,a,b)
