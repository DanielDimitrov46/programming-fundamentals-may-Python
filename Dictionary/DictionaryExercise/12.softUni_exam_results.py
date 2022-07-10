language_dict = {}
students_dict = {}
command = input()

while "exam" not in command:
    command = command.split("-")
    if len(command)>2:
        username, language, points = command
    else:
        name,command2 = command
        if "exam" in name:
            break
        else:
            del students_dict[name]
            command = input()
            continue

    if username not in students_dict:
        students_dict[username] = []
    if language not in language_dict:
        language_dict[language] = 0
    language_dict[language] += 1
    students_dict[username].append(int(points))

    command = input()
print("Results:")
for name in students_dict:
    print(f"{name} | {max(students_dict[name])}")
print("Submissions:")
for language in language_dict:
    print(f"{language} - {language_dict[language]}")