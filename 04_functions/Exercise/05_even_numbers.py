def even_numbers(num):
    even = []
    for x in num:
        x = int(x)
        if x % 2 == 0:
            even.append(x)
    return even


numbers = input().split()

print(even_numbers(numbers))