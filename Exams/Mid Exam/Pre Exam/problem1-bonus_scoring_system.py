number_of_the_students = int(input())
number_of_lectures = int(input())
additional_points = int(input())
max_bonus = 0
max_attendance = 0

for student in range(1,number_of_the_students+1):
    attendance_of_students = int(input())
    total_bonus = round((attendance_of_students/number_of_lectures)*(5+additional_points))
    if total_bonus>max_bonus:
        max_bonus=total_bonus
        max_attendance = attendance_of_students
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendance} lectures.")