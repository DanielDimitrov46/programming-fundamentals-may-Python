number_of_people = int(input())
wagons_list = [int(x) for x in input().split()]
counter =0
flag = True

for current_wagon in wagons_list:
    if current_wagon== 0:
        if number_of_people>=4: 
            number_of_people-=4
            current_wagon+=4
        else:
            current_wagon+=number_of_people
            number_of_people = 0
        wagons_list[counter] += current_wagon
    else:
        difference = 4-current_wagon
        current_wagon+=difference
        number_of_people-=difference
        wagons_list[counter] = current_wagon
    counter+=1 
if number_of_people>0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
    print(' '.join([str(num) for num in wagons_list]))
elif sum(wagons_list)!=len(wagons_list)*4:
    print("The lift has empty spots!")
    print(' '.join([str(num) for num in wagons_list]))
else:
    print(' '.join([str(num) for num in wagons_list]))