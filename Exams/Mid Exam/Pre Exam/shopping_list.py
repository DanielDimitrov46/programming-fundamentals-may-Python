list_of_groceries = input().split("!")
line = input()

while line != "Go Shopping!":
    products = line.split()
    command = products[0]
    product = products[1]
    if "Urgent" in command:
        if product in list_of_groceries:
            line = input()
            continue
        list_of_groceries.insert(0,product)
    elif "Unnecessary" in command:
        if product in list_of_groceries:
            list_of_groceries.remove(product)
    elif "Correct" in command:
        product2 = products[2]
        if product in list_of_groceries:
            index_counter = list_of_groceries.index(product)
            list_of_groceries.remove(product)
            list_of_groceries.insert(index_counter,product2)
    else:
        if product in list_of_groceries:
            list_of_groceries.remove(product)
            list_of_groceries.append(product)
    line = input()
print(", ".join(list_of_groceries))
