number_of_orders = int(input())
total=0

for _ in range(0,number_of_orders):
    forDay=0
    ppc= float(input())
    days= int(input())
    capsulesNeeded= int(input())
    if (ppc<0.01 or ppc>100) or (days<1 or days>31) or (capsulesNeeded<1 or capsulesNeeded>2000):
        continue
    forDay+= (capsulesNeeded*ppc)*days
    total+=forDay
    print(f"The price for the coffee is: ${forDay:.2f}")

print(f"Total: ${total:.2f}")