string_input = input()
vowels = ['a', 'o', 'u', 'e', 'i']
removed_vowels = [x for x in string_input if x.lower() not in vowels]
print(''.join(removed_vowels))
