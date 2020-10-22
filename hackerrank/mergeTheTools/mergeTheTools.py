def merge_the_tools(string, k):
    arr = []
    i = 0
    while i < len(string):
        arr.append(string[i:i+k])
        i += k

    for i in arr:
        d = {}
        for j in i:
            d[j] = d.get(j, 0) + 1
        print(''.join(d.keys()))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)