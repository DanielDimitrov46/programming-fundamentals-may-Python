text = input().upper()
current_symbol = ""
unique_symbol = ""
number = ""

for current_char1 in text:
    if not current_char1.isdigit():
        current_symbol += current_char1
    else:
        for current_char in range(text.index(current_char1), len(text)):
            if not text[current_char].isdigit():
                break
            number += text[current_char]
        number = int(number)
        unique_symbol += number * current_symbol
        current_symbol = ""
        number = ""
print(f"Unique symbols used: {len(set(unique_symbol))}")
print(unique_symbol)
