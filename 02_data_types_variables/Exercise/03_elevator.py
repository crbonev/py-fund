a = int(input())        # a = number of people
b = int(input())        # b = elevator capacity
courses = 0
if b != 0:
    courses = int(a / b)
    if a % b != 0:
        courses += 1
print(courses)