#
# 90/100
# Idk what the issue is.
#
#

cars = input().split()
left_car = cars[:len(cars)//2]
right_car = cars[(len(cars)//2) + 1:]
left_time = 0
right_time = 0

for time1 in left_car:
    digit1 = int(time1)
    if digit1 == 0:
        left_time *= 0.8
    left_time += digit1


for time2 in right_car:
    digit2 = int(time2)
    if digit2 == 0:
        right_time *= 0.8
    right_time += digit2

if left_time < right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
else:
    print(f'The winner is right with total time: {right_time:.1f}')
