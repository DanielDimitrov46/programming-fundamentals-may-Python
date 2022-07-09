students_info = input()

students_dic = {}

while not students_dic.get(students_info):
    students_info = students_info.split(":")
    name_student = students_info[0]
    id_student = students_info[1]
    course_student = students_info[-1]
    if course_student not in students_dic:
        students_dic[course_student]={}
    students_dic[course_student][name_student] = id_student
    students_info = input()
    students_info = students_info.replace("_"," ")

for key,value in students_dic[students_info].items():
    print(f"{key} - {value}")