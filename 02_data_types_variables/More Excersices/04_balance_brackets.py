lines = int(input())
balanced = 0
total = 0
while total < lines:
    total += 1
    string = input()

    if string == "(":
        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()

    elif string == ")":
        balanced -= 1

if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")