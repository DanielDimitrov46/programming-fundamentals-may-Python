version_to_be_updated = [int(x) for x in input().split(".")]

version_to_be_updated[-1] += 1
for index in range(len(version_to_be_updated) - 1, -1, -1):
    if version_to_be_updated[index] > 9:
        version_to_be_updated[index] = 0
        if index - 1 >= 0:
            version_to_be_updated[index - 1] += 1
print(".".join(str(number) for number in version_to_be_updated))