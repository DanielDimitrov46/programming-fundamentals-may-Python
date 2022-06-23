initial_energy = int(input())
won_battles_counter = 0

command = input()

while command != "End of battle":
    distance = int(command)
    if initial_energy >= distance:
        initial_energy -= distance
        won_battles_counter += 1
    else:
        print(f"Not enough energy! Game ends with {won_battles_counter} won battles and {initial_energy} energy")
        break
    if won_battles_counter % 3 == 0:
        initial_energy += won_battles_counter
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_battles_counter}. Energy left: {initial_energy}")
