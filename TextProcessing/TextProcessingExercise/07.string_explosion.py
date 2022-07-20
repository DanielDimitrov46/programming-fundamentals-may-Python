string = input()
final_text = ""
strenght = 0

for index,char in enumerate(string):
    if ">" == char:
        strenght+= int(string[index+1])
        final_text += char
    elif ">" != char and strenght > 0:
        strenght-=1
    else:
        final_text+= char
print(final_text)