# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    k = abs(z-x)
    j = abs(z-y)

    if k>j:
        return "Cat B"
    elif k<j:
        return "Cat A"
    else:
        return "Mouse C"
if __name__ == '__main__':
    

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)