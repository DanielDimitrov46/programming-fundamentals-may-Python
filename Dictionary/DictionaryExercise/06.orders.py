products_dict = {}
products = input().split()

while products[0] != "buy":
    product = products[0]
    price = float(products[1])
    quantity = int(products[2])
    if product not in products_dict:
        products_dict[product] = [price, quantity]
    else:
        products_dict[product][0]=price
        products_dict[product][1]+=quantity

    products = input().split()
for result in products_dict:
    products_dict[result] = products_dict[result][0]*products_dict[result][1]
for key,value in products_dict.items():
    print(f"{key} -> {value:.2f}")