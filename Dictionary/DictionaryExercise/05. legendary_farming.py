useful_items = {"shards": 0, "fragments": 0, "motes": 0}
useless_items = {}
obtained = False
command = input().split()

while True:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key == "shards" or key == "fragments" or key == "motes":
            useful_items[key] += value
        else:
            if key not in useless_items.keys():
                useless_items[key] = value
            else:
                useless_items[key] += value
        if useful_items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            useful_items["shards"] -= 250
            obtained = True
        elif useful_items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            useful_items["fragments"] -= 250
            obtained = True
        elif useful_items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            useful_items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    command = input().split()
for key,value in useful_items.items():
    print(f"{key}: {value}")
for material, quantity in useless_items.items():
    print(f"{material}: {quantity}")