command = input()
coffes=0
realCommand=""
flag = False

while command!="END":
    if command.isupper():
        flag = True
    realCommand= command.lower()
    if realCommand=="coding":
        coffes+=1
    elif realCommand=="dog" or realCommand=="cat":
        coffes+=1
    elif realCommand=="movie":
        coffes+=1
    else:
        command= input()
        continue
    if command.isupper():
        coffes+=1
    command = input()
if coffes>5:
    print("You need extra sleep")
else:
    print(coffes)
