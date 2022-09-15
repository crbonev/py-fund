group_size = int(input())
trip_days = int(input())

total_coins = 0
coins_per_day = 50
coins_person = 0


for current_day in range(1, trip_days + 1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    if current_day % 3 == 0:
        total_coins -= 3 * group_size
    if current_day % 5 == 0:
        total_coins += 20 * group_size
        if current_day % 3 == 0:
            total_coins -= group_size * 2

    total_coins += coins_per_day
    total_coins -= group_size * 2
while total_coins % group_size != 0:
    total_coins -= 1
coins_person = total_coins / group_size

print(f"{group_size} companions received {coins_person:.0f} coins each.")