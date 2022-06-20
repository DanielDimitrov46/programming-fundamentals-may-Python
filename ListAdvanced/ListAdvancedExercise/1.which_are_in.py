string_to_be_found = input().split(", ")
all_strings = input().split(", ")
substrings = []

for element in string_to_be_found:
    for element2 in all_strings:
        if element in element2 and not element in substrings:
            substrings.append(element)
            break

print(substrings)