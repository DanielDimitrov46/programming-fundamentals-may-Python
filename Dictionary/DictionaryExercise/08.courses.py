command = input().split(" : ")
course_dict = {}

while command != "end":
   if len(command)>1:
      course, name = command
   else:
      break
   if course not in course_dict:
      course_dict[course] = []
   course_dict[course].append(name)
   command = input().split(" : ")

for key in course_dict:
   print(f"{key}: {len(course_dict[key])}")
   for names in course_dict[key]:
      print(f"-- {names}")