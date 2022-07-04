food_quantity=float(input()) * 1000
hay_quantity=float(input()) * 1000
cover_quantity=float(input()) * 1000
guinea_weight=float(input()) * 1000
days= 1
#day_counter=0
 
while days <= 30:
 
    food_quantity -= 300
 
    if days % 3 == 0:
        cover_quantity -= guinea_weight * (1/3)
 
    if days % 2 == 0:
        #current_food = 0.3
        #food_quantity -= current_food
        hay_quantity -= food_quantity * 0.05
 
    days += 1
food_quantity = food_quantity / 1000
hay_quantity = hay_quantity / 1000
cover_quantity = cover_quantity / 1000
 
if food_quantity >= 0 and hay_quantity >= 0 and cover_quantity >=0:
 
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
else:
    print("Merry must go to the pet store!")
 
 