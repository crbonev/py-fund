number = int(input())


def is_perfect(numbers):
    total = 0
    for i in range(1, numbers):
        if numbers % i == 0:
            total += i
    if total == numbers:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


print(is_perfect(number))
