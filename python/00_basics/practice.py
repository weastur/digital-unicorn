# 1
a = 42

# 2
s = input()
print(s)

# 3
s = input()
print(len(s))

# 4a
a = int(input())
print('Пользователь ввел', a)

# 4b
a = int(input())
print(f'Пользователь ввел {a}')

# 5
a = float(input('Введите длину стороны 1 '))
b = float(input('Введите длину стороны 2 '))
print('Площадь', a * b)

# 6
print('Площадь', float(input('Введите длину стороны 1 ')) * float(input('Введите длину стороны 2 ')))

# 7
a = int(input())
b = int(input())
print('Введено {0} потом {1}, сначала {0} потом {1}'.format(a, b))

# 8
a = int(input())
if a & 1:
    print('Нечетное')
else:
    print('Четное')

b = int(input())
print(1 << b) # 2 в степени b

# 9
a = int(input())
b = int(input())
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if a == 0:
    print(0)
else:
    ans = ''
    while a > 0:
        ans = alphabet[a % b] + ans
        a = a // b
    print(ans)

# 10
l = 1
r = 100
print(f'Загадайте число в диапазоне [{l};{r}]')
while l != r:
    if r - l == 1:
        m = r
    else:
        m = l + (r - l) // 2
    while True:
        ans = input(f'Загаданное число равно, больше либо меньше {m}? (= > <)? ')
        if ans == '=':
            print('Игра окончена')
            exit(0)
        elif ans == '>':
            l = m
            break
        elif ans == '<':
            r = m
            break
        else:
            print('Некорректный ответ')
print('Нечестная игра')

##########################################################################
# 11

def calc(expr):
    plus_pos = expr.find('+')
    minus_pos = expr.find('-')
    multiply_pos = expr.find('*')
    int_division_pos = expr.find('//')
    mod_pos = expr.find('%')
    power_pos = expr.find('**')
    if power_pos != -1:
        return int(expr[0:power_pos]) ** int(expr[power_pos + 2:])
    elif int_division_pos != -1:
        return int(expr[0:int_division_pos]) // int(expr[int_division_pos + 2:])
    elif mod_pos != -1:
        return int(expr[0:mod_pos]) % int(expr[mod_pos + 1:])
    elif multiply_pos != -1:
        return int(expr[0:multiply_pos]) * int(expr[multiply_pos + 1:])
    elif minus_pos != -1:
        return int(expr[0:minus_pos]) - int(expr[minus_pos + 1:])
    elif plus_pos != -1:
        return int(expr[0:plus_pos]) + int(expr[plus_pos + 1:])


expression = input().replace(' ', '')
while True:
    if expression.isnumeric():
        print(expression)
        break
    if expression.find('(') == -1 and expression.find(')') == -1:
        expression = str(calc(expression))
        continue
    bracket_pos = -1
    current_pos = 0
    while current_pos < len(expression):
        if expression[current_pos] == '(':
            bracket_pos = current_pos
        elif expression[current_pos] == ')':
            expression = expression[0:bracket_pos] + str(calc(expression[bracket_pos + 1:current_pos])) + expression[current_pos + 1:]
            break
        current_pos += 1