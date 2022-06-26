number_of_cities = int(input())
total =0
global_total = 0
for city in range(1,number_of_cities+1):
    additional_costs = 0
    name_of_city = input()
    owners_income = float(input())
    owners_expenses = float(input())
    if city%3==0:
        additional_costs+=owners_expenses*0.5
    if city%5==0:
        owners_income-=owners_income*0.10
        if city%3==0:
            additional_costs=0
    total = owners_income-(owners_expenses+additional_costs)
    global_total+=total
    print(f"In {name_of_city} Burger Bus earned {total:.2f} leva.")
print(f"Burger Bus total profit: {global_total:.2f} leva.")