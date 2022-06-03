budget = float(input())
price_Per_Flour = float(input())
counter = 0
total_budget=0
colored_eggs=0
price_Eggs_Pack = 0.75*price_Per_Flour
price_Milk_Liter = (price_Per_Flour+price_Per_Flour*0.25)*0.25
price_For_One_Loaf = price_Eggs_Pack+ price_Milk_Liter+price_Per_Flour
total_budget+=price_For_One_Loaf
while budget>= total_budget:
    total_budget+=price_For_One_Loaf
    colored_eggs+=3
    counter+=1
    if counter%3==0:
        colored_eggs-= (counter - 2)
diff = budget - (total_budget-price_For_One_Loaf)
print(f"You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {diff:.2f}BGN left.")