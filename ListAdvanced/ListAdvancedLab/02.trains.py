number_of_wagons = int(input())
list_of_wagons = [0]*number_of_wagons

command = input().split()
while "End" not in command:
    if "add" in command:
        list_of_wagons[number_of_wagons-1]+=int(command[1])
    elif "insert" in command:
        list_of_wagons[int(command[1])]+=int(command[2])
    elif "leave" in command:
        list_of_wagons[int(command[1])]-=int(command[2])
    command = input().split()

print(list_of_wagons)