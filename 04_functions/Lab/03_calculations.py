def calculate(a, b, operator):
    if operator == 'multiply':
        return multiply(a, b)
    elif operator == 'divide':
        return divide(a, b)
    elif operator == 'add':
        return add(a, b)
    elif operator == 'subtract':
        return subtract(a, b)


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    result = int(a / b)
    return result


def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


operator_input = input()
first = int(input())
second = int(input())

print(calculate(first, second, operator_input))
