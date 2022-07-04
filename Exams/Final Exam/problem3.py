list_of_phones = input().split(", ")
line = input()

while line!="End":
    cmd = line.split(" - ")
    command = cmd[0]
    phone = cmd[1]
    if "Add" in command:
        if phone in list_of_phones:
            line = input()
            continue
        list_of_phones.append(phone)
    elif "Remove" in command:
        if phone in list_of_phones:
            list_of_phones.remove(phone)
    elif "Bonus phone" in command:
        cmd2 = phone.split(":")
        old_phone = cmd2[0]
        new_phone = cmd2[1]
        if old_phone in list_of_phones:
            list_of_phones.insert(list_of_phones.index(old_phone)+1,new_phone)
    else:
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)
    line = input()
print(", ".join(list_of_phones))