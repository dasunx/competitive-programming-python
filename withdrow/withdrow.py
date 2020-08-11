money = int(input())
count = 0

if money / 100 > 0:
    count += int(money / 100)
    money %= 100
if money / 20 > 0:
    count += int(money / 20)
    money %= 20
if money / 10 > 0:
    count += int(money / 10)
    money %= 10
if money / 5 > 0:
    count += int(money / 5)
    money %= 5
if money > 0:
    count += money
    money = 0

print(count)
