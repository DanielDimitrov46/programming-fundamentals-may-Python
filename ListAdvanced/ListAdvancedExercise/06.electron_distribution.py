number_of_electrons = int(input())
list_of_filled_shells = []
shell = 1
while number_of_electrons>0:
    for_ejection = 2*(shell**2)
    if number_of_electrons<for_ejection:
        for_ejection = number_of_electrons
    list_of_filled_shells.append(int(for_ejection))
    number_of_electrons-=for_ejection
    shell+=1
print(list_of_filled_shells)