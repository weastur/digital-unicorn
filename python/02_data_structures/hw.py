# 1
n = int(input())
a = []
for i in range(n):
    a.append(input())
k = int(input())
if k:
    print(' '.join(a[-k:] + a[:len(a) - k]))
else:
    print(' '.join(a))

# 2
n = int(input())
a = set()
for i in range(n):
    a.add(int(input()))
m = int(input())
b = set()
for i in range(m):
    b.add(int(input()))
c = []
for item in sorted(a & b):
    c.append(str(item))
print(' '.join(sorted(c)))

# 3
cities = {}
n = int(input())
for i in range(n):
    country = input()
    m = int(input())
    for j in range(m):
        cities[input()] = country

k = int(input())
for i in range(k):
    print(cities.get(input(), -1))

# 4
n = int(input())
d = {}
for _ in range(n):
    data = input()
    key, value = data.split(':')
    d[key] = value
for key in sorted(d.keys()):
    print(f'{key}:{d[key]}')