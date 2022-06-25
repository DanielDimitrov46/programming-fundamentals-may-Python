# command = input()
# total = 0
# while command != "special":
#     if command == "regular":
#         break
#     parts_price_without_tax = float(command)
#     if parts_price_without_tax <= 0:
#         print("Invalid price!")
#         command = input()
#         continue
#     total += parts_price_without_tax
#     command = input()
#
# tax = total * 0.2
# final_price = total + tax
# if command == "special":
#     if final_price == 0:
#         print("Invalid order!")
#     else:
#         final_price -= final_price * 0.1
#         print("Congratulations you've just bought a new computer!")
#         print(f"Price without taxes: {total:.2f}$")
#         print(f"Taxes: {tax:.2f}$")
#         print("-----------")
#         print(f"Total price: {final_price:.2f}$")
# else:
#     if final_price == 0:
#         print("Invalid order!")
#     else:
#         print("Congratulations you've just bought a new computer!")
#         print(f"Price without taxes: {total:.2f}$")
#         print(f"Taxes: {tax:.2f}$")
#         print("-----------")
#         print(f"Total price: {final_price:.2f}$")

line = input()
net_price = 0

while line!="special" and line!="regular":
    current_price = float(line)

    if current_price>0:
        net_price+=current_price
    else:
        print("Invalid price!")

    line = input()

if net_price<=0:
    print('Invalid order!')
else:
    taxes = net_price*0.2
    final_price = net_price+taxes

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")

    if line=="special":
        final_price = final_price*0.9

    print(f"Total price: {final_price:.2f}$")