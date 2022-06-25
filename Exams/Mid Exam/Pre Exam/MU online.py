# max_health = 100
# is_dead = False
#
# rooms = input().split('|')
#
# health = max_health
# bitcoins = 0
# best_room = 0
#
# for current_room in range(len(rooms)):
#     best_room += 1
#     command=rooms[current_room]
#     tokens=command.split()
#
#     if tokens[0] == 'potion':
#         health_points = int(tokens[1])
#         if health + health_points > max_health:
#             health_points = max_health - health
#             health = max_health
#         else:
#             health += health_points
#         print(f'You healed for {health_points} hp.')
#         print(f'Current health: {health} hp.')
#
#     elif tokens[0] == 'chest':
#         amount = int(tokens[1])
#         print(f'You found {amount} bitcoins.')
#         bitcoins += amount
#     else:
#         monster = tokens[0]
#         attack = int(tokens[1])
#         health -= attack
#         if health > 0:
#             print(f'You slayed {monster}.')
#         else:
#             print(f'You died! Killed by {monster}.')
#             print(f'Best room: {best_room}')
#             is_dead = True
#             break
#
# if not is_dead:
#     print(f"You've made it!")
#     print(f"Bitcoins: {bitcoins}")
#     print(f"Health: {health}")

health = 100
bitcoins = 0
is_life = True

dungeons_rooms = input().split("|")
best_room = 1
for room in dungeons_rooms:
    current_room = room.split()
    command = current_room[0]
    number = int(current_room[1])
    if command=="potion":
        health+=number
        if health>100:
            diff = health-100
            health = health-diff
            number-=diff
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command=="chest":
        bitcoins+=number
        print(f"You found {number} bitcoins.")
    else:
        health-=number
        if health>0:
            print(f"You slayed {command}.")
        else:
            is_life = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break
    best_room+=1

if is_life:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
