number_of_commands = int(input())
register_dict = {}

for _ in range(0,number_of_commands):
    command = input().split()
    if command[0] =="register":
        type, username, plate = command
        if username not in register_dict:
            register_dict[username] = plate
            print( f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    else:
        type, username = command
        if username not in register_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del register_dict[username]

for key,value in register_dict.items():
    print(f"{key} => {value}")


