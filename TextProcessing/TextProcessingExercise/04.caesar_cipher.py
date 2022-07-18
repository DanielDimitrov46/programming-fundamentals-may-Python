text = input()
final_text=""

for character in text:
    character = ord(character)+3
    final_text+=chr(character)
print(final_text)