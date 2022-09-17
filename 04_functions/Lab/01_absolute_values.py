# numbers = input().split()
# digits = []
# for digit in numbers:
#     digits.append(abs(float(digit)))
# print(digits)

numbers = input().split()


def absolute(num):
    digits = []
    for digit in num:
        digits.append(abs(float(digit)))
    return digits


print(absolute(numbers))
