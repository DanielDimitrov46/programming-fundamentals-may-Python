from math import floor

group_size = int(input())
days = int(input())
coins_counter = 0

for days_counter in range(1, days + 1):
    if days_counter % 10 == 0:
        group_size -= 2
    if days_counter % 15 == 0:
        group_size += 5
    if days_counter % 3 == 0:
        coins_counter -= group_size * 3
    if days_counter % 5 == 0:
        coins_counter += group_size * 20
        if days_counter % 3 == 0:
            coins_counter -= group_size * 2
    coins_counter += 50
    coins_counter -= group_size * 2
coins_per_companion = floor(coins_counter / group_size)
print(f"{group_size} companions received {coins_per_companion} coins each.")
