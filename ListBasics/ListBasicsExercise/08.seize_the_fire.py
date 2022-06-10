sort_of_fire = input().split("#")
amount_of_water = int(input())
put_out_cells = []
effort = 0

for element in sort_of_fire:
    current_cell = element.split()
    type_of_fire = current_cell[0]
    value_of_fire = int(current_cell[4])
    if amount_of_water<=0:
        break
    if (type_of_fire == "High") and (81 <= value_of_fire <= 125):
        amount_of_water-=value_of_fire
        #effort+=0.25*value_of_fire
    else:
        pass

    if (type_of_fire == "Medium") and (51 <= value_of_fire <= 80):
        amount_of_water-=value_of_fire
    else:
        pass

    if (type_of_fire == "Low") and (1 <= value_of_fire <= 50):
        amount_of_water-=value_of_fire
    else:
        pass
