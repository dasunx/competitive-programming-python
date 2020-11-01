def mutate_string(string, position, character):

    x = list(string)
    x[position] = character
    string = ''.join(x)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
