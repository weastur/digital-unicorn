# 1
n = int(input())
if n < 7:
    print('Yes')
elif n > 10:
    print('No')
elif n == 9:
    print('Error')

# 2
n = int(input())
if n == 1:
    print('January')
elif n == 2:
    print('February')
elif n == 3:
    print('March')
elif n == 4:
    print('April')
elif n == 5:
    print('May')
elif n == 6:
    print('June')
elif n == 7:
    print('July')
elif n == 8:
    print('August')
elif n == 9:
    print('September')
elif n == 10:
    print('October')
elif n == 11:
    print('November')
elif n == 12:
    print('December')

# 3
ch = input()
alphabet = 'abcdefghijklmnopqrstuvwxyzabc'
position = ord(ch.lower()) - ord('a')
print(alphabet[position+1:position+4])

# 4
for x in range(1000, 10000):
    s = str(x)
    if s[0] != s[1] and s[0] != s[2] and s[0] != s[3] and s[1] != s[2] and s[1] != s[3] and s[2] != s[3]:
        print(s)
# 5
for x in range(1000, 10000):
    s = str(x)
    if '5' not in s and '6' not in s:
        print(s)

# 6
for x in range(1000, 10000):
    s = str(x)
    if '3' in s:
        print(s)

# 7
result = 0
for x in range(1000, 10000):
    s = str(x)
    sum = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3])
    if sum * 600 == x:
        result += 1
print(result)

# 8
s = 0
while True:
    x = int(input())
    s += x
    if x == 0:
        break
print(s)

# 9
x = 11
while True:
    if x % 11 == 0 and x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1 and x % 7 == 1 and x % 8 == 1 and x % 9 == 1 and x % 10 == 1:
        print(x)
        break
    x += 1

# 10
n = int(input())
print('1 ' * n)
print('2 ' * 2 * n)
print('3 ' * 3 * n)

# 11
print(1)
for x in range(2, 10001):
    sum = 0
    n = x
    while n > 0:
        sum += n % 10
        n //= 10
    d = 1
    if sum == 1:
        continue
    while d <= x:
        if d == x:
            print(x)
            break
        d *= sum

# 12
import random
import string
password = ['_'] + random.choices(string.ascii_uppercase, k=random.randint(2, 5)) + random.choices(string.digits, k=random.randint(1, 5)) + random.choices(string.ascii_lowercase, k=random.randint(2, 5))
while True:
    random.shuffle(password)
    good = True
    for i in range(len(password) - 1):
        if password[i].isdigit() and password[i + 1].isdigit():
            good = False
            break
    if good:
        break
print(''.join(password))