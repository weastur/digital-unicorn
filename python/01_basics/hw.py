# 2
a = int(input())
b = int(input())
c = int(input())
result = 0
if a > 0:
    result += 1
if b > 0:
    result += 1
if c > 0:
    result += 1
print(result)

# 3
a = int(input())
b = int(input())
c = int(input())
if a + b == c or a + c == b or b + c == a:
    print('yes')
else:
    print('no')

# 4
n = int(input())
result = 1
while n > 0:
    result *= n % 10
    n //= 10
print(result)

# 5
n = int(input())
result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10
print(result)

# 6
n = int(input())
m = 0
result = 0
while n > 0:
    if not (1000 > n >= 100):
        m = m * 10 + n % 10
    n //= 10
while m > 0:
    result = result * 10 + m % 10
    m //= 10
print(result)

# 7
a = int(input())
b = int(input())
result = 0
for x in range(a, b + 1):
    if x == 2:
        result += 1
        continue
    d = 2
    is_prime = True
    while d * d <= x:
        if x % d == 0:
            is_prime = False
            break
        d += 1
    if is_prime:
        result += 1
print(result)

# 8
for i in range(10, 0, -1):
    print(f'{i} ' * i, end='')

# 9
n = int(input())
for i in range(1, n + 1):
    print('*' * i)

# 10
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 1:
        print('*' * 7)
    else:
        print('*' * 4)

# 11
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            print(0, end='')
        else:
            print(1, end='')
    print()

# 12
for i in range(1, 21):
    if i % 2 == 1:
        print('1 ' * 10)
    else:
        print(f'{i} ' * 10)

# 13
n = int(input())
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a = 0
    b = 1
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    print(b)

# 14
a = int(input())
b = int(input())
result = 0
for i in range(a, b + 1):
    si = 0
    for d in range(1, i):
        if i % d == 0:
            si += d
    for j in range(i + 1, b + 1):
        sj = 0
        for d in range(1, j):
            if j % d == 0:
                sj += d
        if si == j and sj == i:
            result += 1
print(result)

# 15
n = int(input())
for x in range(2, n):
    s = 0
    for d in range(1, x):
        if x % d == 0:
            s += d
    if s == x:
        print(x)
