if __name__ == '__main__':

    n = int(input())
    b = input()
    a = tuple(map(int, b.split(' ')))
    if len(a) == n:
        print(hash(a))
    else:
        print('you have exceeded your limit')
