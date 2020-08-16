# 1
a = int(input())
b = int(input())
result = a if a > b else b
print(result)

# 2
a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print('a кратно 15')
else:
    print('а не кратно 15')

# 3
a = int(input())
b = int(input())
c = int(input())
if a == b or b == c or a == c:
    print('yes')
else:
    print('ERROR')

# 4
s1 = input()
for ch in s1:
    print(ch)

# 5
while True:
    ch = input('Для продолжения введите „y“. Для выхода любой другой символ')
    if ch != 'y':
        break

# 6
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
print(s)

# 7
n = int(input())
if n == 2:
    print('Yes')
else:
    is_prime = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            is_prime = False
            break
        d += 1
    if is_prime:
        print('Yes')
    else:
        print('No')

# 8
n = int(input())
d = 2
while d * d <= n:
    while n % d == 0:
        print(d, end=' ')
        n //= d
    d += 1
if n != 1:
    print(n)