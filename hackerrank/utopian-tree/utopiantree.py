#!/bin/python3

# Complete the utopianTree function below.
def utopianTree(n):
    h = 1 
    for i in range(n):
        if i %2 !=0:
            h+=1
        else:
            h*=2
    return h
if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(str(result) + '\n')

 
