numbers = list(map(int, input().split()))


def minimum(num):
    return f"The minimum number is {min(num)}"


def maximum(num):
    return f"The maximum number is {max(num)}"


def sum_of(num):
    return f"The sum number is: {sum(num)}"


print(minimum(numbers))
print(maximum(numbers))
print(sum_of(numbers))

