lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet = 0
sword = 0
shield = 0
armor = 0


for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        helmet += 1
    if fight % 3 == 0:
        sword += 1
        if fight % 2 == 0:
            shield += 1
            if shield % 2 == 0:
                armor += 1
total = armor * armor_price + sword * sword_price + helmet_price * helmet + shield_price * shield
print(f'Gladiator expenses: {total:.2f} aureus')