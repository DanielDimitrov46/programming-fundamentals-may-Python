gifts = input().split()
command = input()

while command != "No Money":
    if "OutOfStock" in command:
        out_of_stock = command.split()
        for i, name in enumerate(gifts):
            if out_of_stock[-1] == name:
                gifts[i] = "None"

    elif "Required" in command:
        required = command.split()
        length = len(gifts)
        if length > int(required[-1]) >= 0:
            gifts[int(required[-1])] = required[1]

    elif "JustInCase" in command:
        just_in_case = command.split()
        gifts[-1] = just_in_case[-1]
    command = input()
print(" ".join(x for x in gifts if x != "None"))