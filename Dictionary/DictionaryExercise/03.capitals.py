countries = input().split(", ")
capitals = input().split(", ")

result = {countries[index] : capitals[index] for index in range(0,len(countries))}

for country, capital in result.items():
    print(f"{country} -> {capital}")