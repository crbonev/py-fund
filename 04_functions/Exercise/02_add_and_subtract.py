
def add_and_subtract(a, b, c):

    def sum_numbers():
        return a + b

    def subtract():
        return sum_numbers() - c

    return subtract()


one = int(input())
two = int(input())
three = int(input())

print(add_and_subtract(one, two, three))