items = input().split(", ")
line = input()

while line!= "Craft!":
    cmd = line.split(" - ")
    command = cmd[0]
    material = cmd[1]
    if command=="Collect":
        if material in items:
            continue
        items.append(material)
    elif command =="Drop":
        if material in items:
            items.remove(material)
    elif command == "Combine Items":
        cmd2 = material.split(":")
        old_item = cmd2[0]
        new_item = cmd2[1]
        if old_item in items:
            items.insert(items.index(old_item)+1,new_item)
    else:
        if material in items:
            items.remove(material)
            items.append(material)
    line = input()
print(", ".join(items))