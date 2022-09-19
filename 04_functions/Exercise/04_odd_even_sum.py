number = str(input())


def sum_odd_even(num):
    even = 0
    odd = 0
    for x in num:
        b = int(x)
        if b % 2 == 0:
            even += b
        else:
            odd += b
    return f'Odd sum = {odd}, Even sum = {even}'


print(sum_odd_even(number))
