budget = int(input())
product = input()
total=0

while product!="End":
    productPrice = int(product)
    total+=productPrice
    if total>budget:
        print("You went in overdraft!")
        break

    product = input()
else:
    print("You bought everything needed.")