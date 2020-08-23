from bisect import bisect_right

n = int(input())
scores = sorted(set(map(int, input().split())))
m = int(input())
alice = map(int, input().split())

# your code goes here
for i in alice:
    print(len(scores) - bisect_right(scores, i) + 1)

