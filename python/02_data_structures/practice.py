# 1
n = int(input())
a = []
for i in range(n):
    if i == 0 or i == n - 1:
        a.append(1)
    else:
        a.append(0)
print(a)

# 2
n = int(input())
a = []
for i in range(n):
    a.append(i * i)
print(a)

# 3
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(max(a) + min(a))

# 4
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
equals_exists = False
for i in range(n - 1):
    if a[i] == a[i + 1]:
        equals_exists = True
        break
if equals_exists:
    print("YES")
else:
    print("NO")

# 5
a = {}
b = dict()

person = {'first_name': None, 'last_name': None}
print(person)

person.update({'first_name': 'Pavel', 'last_name': 'Sapezhko'})
print(person)

person['age'] = -1
print(person)

print(list(person.keys()))
print(list(person.values()))

# 6
subdivision = ('Brest', 'Homel', 'Grodno', 'Mogilev', 'Minsk', 'Vitebsk')
population = (1401177, 1440718, 1072381, 1099074, 1422528, 1230821)
population_dict = {}
for i in range(len(subdivision)):
    population_dict[subdivision[i]] = population[i]
print(population_dict)

print('Сумма по всем областям:', sum(population_dict.values()))

max_subdivision = subdivision[0]
for current_subdivision in population_dict:
    if population_dict[current_subdivision] > population_dict[max_subdivision]:
        max_subdivision = current_subdivision
print(f'Область: {max_subdivision}, Население: {population_dict[max_subdivision]}')

avg = sum(population_dict.values()) / len(population_dict)
print('Среднее:', avg)

closest_subdivision = subdivision[0]
for current_subdivision in population_dict:
    if abs(population_dict[current_subdivision] - avg) < abs(population_dict[closest_subdivision] - avg):
        closest_subdivision = current_subdivision
print('Ближайшее к среднему:', closest_subdivision)