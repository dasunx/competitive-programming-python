# Complete the hurdleRace function below.
def hurdleRace(k, height):
    height.sort()
    y = height[len(height) - 1] - k
    if y > 0:
        return y
    return 0


if __name__ == "__main__":

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(str(result))

