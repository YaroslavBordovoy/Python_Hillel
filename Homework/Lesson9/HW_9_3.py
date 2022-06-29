# Игра в города

cities = input('Please enter a list of cities: ').lower().split()

def chains(cities, previous_city = None):
    yield []
    cities = [city for city in cities if city != previous_city]
    for each_city in cities:
        if not previous_city or each_city.startswith(previous_city[-1]):
            for lain in chains(cities, previous_city = each_city):
                yield [each_city] + lain

all_sequences = list(chains(cities))
all_sequences.sort(key=len)

print('Longest sequence: ', max(chains(cities), key=len))
