n = int(input())
str = input()

comp_string = ""
l = 0

for i in range(n):
    print(str[i])
    if comp_string == "":
        if str[i] == "S":
            comp_string = "S"
    elif comp_string == "S":
        if str[i] == "L":
            comp_string = "SL"
    elif comp_string == "SL":
        if str[i] == "I":
            comp_string = "SLI"
    elif comp_string == "SLI":
        if str[i] == "I":
            comp_string = "SLII"
    elif comp_string == "SLII":
        if str[i] == "T":
            l += 1
            comp_string = ""

print(l)
