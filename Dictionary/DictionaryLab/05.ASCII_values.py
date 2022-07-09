characters = input().split(", ")
ascii_dict=dict()

for letter in characters:
    ascii_dict[letter] = ord(letter)
print(ascii_dict)