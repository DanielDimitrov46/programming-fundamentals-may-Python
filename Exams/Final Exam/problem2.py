all_friends = input().split(", ")
line = input()
blacklisted_counter = 0
lost_names_counter = 0



while line != "Report":
    cmd = line.split()
    command = cmd[0]
    secondary_item = cmd[1]
    if "Blacklist" in command:
        if secondary_item in all_friends:
            index_of_secondary_item = all_friends.index(secondary_item)
            all_friends[index_of_secondary_item] = "Blacklisted"
            blacklisted_counter+=1
            print(f"{secondary_item} was blacklisted.")
        else:
            print(f"{secondary_item} was not found.")
    elif "Error" in command:
        if int(secondary_item)>=0 and int(secondary_item)<len(all_friends):
            name_of_the_index = all_friends[int(secondary_item)]
            if name_of_the_index!="Blacklisted" and name_of_the_index!="Lost":
                all_friends[int(secondary_item)] = "Lost"
                lost_names_counter+=1
                print(f"{name_of_the_index} was lost due to an error.")
    else:
        third_item = cmd[2]
        #
        if int(secondary_item) >= 0 and int(secondary_item) < len(all_friends):
            name_of_the_index = all_friends[int(secondary_item)]
            if name_of_the_index != "Blacklisted" or name_of_the_index != "Lost":
                all_friends[int(secondary_item)] = third_item
                print(f"{name_of_the_index} changed his username to {third_item}.")
    line = input()

print(f"Blacklisted names: {blacklisted_counter}")
print(f"Lost names: {lost_names_counter}")
print(" ".join(all_friends))