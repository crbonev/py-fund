first_number = int(input())
second_number = int(input())


def fact_div(number1, number2):
    factorial1 = 1
    factorial2 = 1
    for i in range(1, number1 + 1):
        factorial1 *= i
    for i2 in range(1, number2 + 1):
        factorial2 *= i2
    result = factorial1 / factorial2
    return f'{result:.2f}'


print(fact_div(first_number, second_number))
