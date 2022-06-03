name = input()
school = ""

while name != "Welcome!":
    numberOfSymbolsInName = 0
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    numberOfSymbolsInName += len(name)
    if numberOfSymbolsInName < 5:
        school = "Gryffindor"
    elif numberOfSymbolsInName == 5:
        school = "Slytherin"
    elif numberOfSymbolsInName == 6:
        school = "Ravenclaw"
    elif numberOfSymbolsInName > 6:
        school = "Hufflepuff"
    
    print(f"{name} goes to {school}.")

    name = input()
else:
    print("Welcome to Hogwarts.")