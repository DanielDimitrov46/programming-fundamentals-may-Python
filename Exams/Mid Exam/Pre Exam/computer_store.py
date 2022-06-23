command = input()
total = 0
while command != "special":
    if command == "regular":
        break
    parts_price_without_tax = float(command)
    if parts_price_without_tax <= 0:
        print("Invalid price!")
        command = input()
        continue
    total += parts_price_without_tax
    command = input()

tax = total * 0.2
final_price = total + tax
if command == "special":
    if final_price == 0:
        print("Invalid order!")
    else:
        final_price -= final_price * 0.1
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print("-----------")
        print(f"Total price: {final_price:.2f}$")
else:
    if final_price == 0:
        print("Invalid order!")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print("-----------")
        print(f"Total price: {final_price:.2f}$")
