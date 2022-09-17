numbers = input().split()


def rounding(num):
    rounded = []
    for number in num:
        rounded.append(round(float(number)))
    return rounded


print(rounding(numbers))