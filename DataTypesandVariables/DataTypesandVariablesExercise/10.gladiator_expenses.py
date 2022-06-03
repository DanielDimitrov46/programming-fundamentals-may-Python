lost_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0

for counter in range(1, lost_count + 1):
    if counter % 2 == 0:
        expenses += helmet_price
    if counter % 3 == 0:
        expenses += sword_price
    if counter % 6 == 0:
        expenses += shield_price
    if counter%12==0:
        expenses+=armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")