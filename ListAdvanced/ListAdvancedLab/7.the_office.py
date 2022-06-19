employees_happines = [int(x) for x in input().split()]
improvement_factor = int(input())

new_list_of_hapiness = []
valid_happiness = []
for employeer in employees_happines:
    new_list_of_hapiness.append(employeer*improvement_factor)
average_happiness = sum(new_list_of_hapiness)/len(employees_happines)
for employer_happiness in new_list_of_hapiness:
    if employer_happiness>= average_happiness:
        valid_happiness.append(employer_happiness)
if len(valid_happiness)>=len(employees_happines)/2:
    print(f"Score: {len(valid_happiness)}/{len(employees_happines)}. Employees are happy!")
else:
    print(f"Score: {len(valid_happiness)}/{len(employees_happines)}. Employees are not happy!")