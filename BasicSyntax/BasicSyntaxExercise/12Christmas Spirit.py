quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
spirit_counter = 0
total_price = 0

for day_counter in range(1, days+1):
    if day_counter % 11 == 0:
        quantity += 2
    if day_counter % 2 == 0:
        total_price += ornament_set*quantity
        spirit_counter += 5
    if day_counter % 3 == 0:
        total_price += (tree_skirt+tree_garland)*quantity
        spirit_counter += 13
    if day_counter % 5 == 0:
        total_price += tree_lights*quantity
        spirit_counter += 17
        if day_counter % 3 == 0:
            spirit_counter += 30
    if day_counter % 10 == 0:
        spirit_counter -= 20
        total_price += tree_skirt+tree_garland+tree_lights

if days % 10 == 0:
    spirit_counter -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {spirit_counter}")
