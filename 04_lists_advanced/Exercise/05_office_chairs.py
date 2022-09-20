rooms = int(input())
current_room = 0
total_chairs = 0
total_people = 0
while rooms > 0:
    rooms -= 1
    current_room += 1
    current = input().split(' ')
    chairs = len(current[0])
    people = int(current[1])
    total_chairs += chairs
    total_people += people

    if chairs < people:
        needed = abs(people - chairs)
        print(f"{needed} more chairs needed in room {current_room}")
    elif people >= chairs:
        total_chairs += people - chairs
total_chairs -= total_people
if total_chairs >= 0:
    print(f"Game On, {total_chairs} free chairs left")

