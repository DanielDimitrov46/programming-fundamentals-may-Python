commands = input().split()
new_list = []

while commands[0]!= "end":
    first_command = commands[0]
    second_command = commands[1]

    if "Chat" in first_command:
        new_list.append(second_command)
    elif "Delete" in first_command:
        if second_command in new_list:
            new_list.remove(second_command)
    elif "Edit" in first_command:
        third_command = commands[2]
        if second_command in new_list:
            index_of_word = new_list.index(second_command)
            new_list[index_of_word] = third_command
    elif "Pin" in first_command:
        if second_command in new_list:
            new_list.remove(second_command)
            new_list.append(second_command)
    else:
        length_of_spam_message = len(commands)
        for item in range(1,length_of_spam_message):
            new_list.append(commands[item])

    commands = input().split()

print("\n".join(new_list))
