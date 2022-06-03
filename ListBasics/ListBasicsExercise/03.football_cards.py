team_a = ["A-1","A-2","A-3","A-4","A-5","A-6","A-7","A-8","A-9","A-10","A-11"]
team_b = ["B-1","B-2","B-3","B-4","B-5","B-6","B-7","B-8","B-9","B-10","B-11"]
game_is_terminated = False
sent_off_players = input().split(" ")

# for letter in range(65,66):
#     if letter == 65:
#         letterA.append(chr(letter))
#     else:
#         letterB.append(chr(letter))
#
# for adding in range(0,11):
#     team_a.append(adding)
#     team_b.append(adding)
# team_a = team_a.append(letterA)
# team_b = team_b.append(letterB)
# print(team_a)
# print(team_b)

# while len(team_a) or len(team_b)<7:
#

for player in sent_off_players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_is_terminated:
    print("Game was terminated")
