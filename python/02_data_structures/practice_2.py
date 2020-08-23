# 1
n = int(input())
a = []
b = []
for i in range(n):
    x = int(input())
    b.append(x)
    b.extend(a)
    a.append(x)
print(b)

# 2
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
m = int(input())
b = []
for i in range(m):
    b.append(int(input()))
equals = True
for x in a:
    if x not in b:
        equals = False
        break
for x in b:
    if x not in a:
        equals = False
        break
if equals:
    print("YES")
else:
    print("NO")

# 3
rows = int(input())
columns = int(input())
a = []
for _ in range(rows):
    row = input().split()
    current_row = []
    for x in row:
        current_row.append(int(x))
    a.append(current_row)
result = 0
for i in range(rows):
    if a[i] == sorted(a[i]):
        result += 1
print(result)

# 4
rows = int(input())
columns = int(input())
a = []
for _ in range(rows):
    row = input().split()
    current_row = []
    for x in row:
        current_row.append(int(x))
    a.append(current_row)
for _ in range(columns):
    for j in range(columns - 1):
        if a[0][j] > a[0][j + 1]:
            for i in range(rows):
                a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
for i in range(rows):
    for j in range(columns):
        print(a[i][j], end=' ')
    print()

# 5
rows = int(input())
columns = int(input())
a = []
for _ in range(rows):
    row = input().split()
    current_row = []
    for x in row:
        current_row.append(int(x))
    a.append(current_row)

maxlen_row_len = 0
maxlen_row_start = 0
maxlen_row_index = 0
for i in range(rows):
    current_len = 0
    for j in range(columns):
        if a[i][j] == 0 and (j == 0 or a[i][j - 1] == 0):
            current_len += 1
        else:
            current_len = 0
        if current_len > maxlen_row_len:
            maxlen_row_index = i
            maxlen_row_len = current_len
            maxlen_row_start = j - current_len + 1

maxlen_col_len = 0
maxlen_col_start = 0
maxlen_col_index = 0
for j in range(columns):
    current_len = 0
    for i in range(rows):
        if a[i][j] == 0 and (i == 0 or a[i - 1][j] == 0):
            current_len += 1
        else:
            current_len = 0
        if current_len > maxlen_col_len:
            maxlen_col_index = j
            maxlen_col_len = current_len
            maxlen_col_start = i - current_len + 1

maxlen_diag_main_len = 0
maxlen_diag_main_start = 0
current_len = 0
for i in range(rows):
    if a[i][i] == 0 and (i == 0 or a[i - 1][i - 1] == 0):
        current_len += 1
    else:
        current_len = 0
    if current_len > maxlen_diag_main_len:
        maxlen_diag_main_len = current_len
        maxlen_diag_main_start = i - current_len + 1

maxlen_diag_secondary_len = 0
maxlen_diag_secondary_start = 0
current_len = 0
for i in range(rows):
    if a[i][columns - i - 1] == 0 and (i == 0 or a[i - 1][columns - i - 2] == 0):
        current_len += 1
    else:
        current_len = 0
    if current_len > maxlen_diag_secondary_len:
        maxlen_diag_secondary_len = current_len
        maxlen_diag_secondary_start = columns - current_len

print(f'По горизонтали. Старт в строке: {maxlen_row_index}, столбец: {maxlen_row_start}, длина: {maxlen_row_len}')
print(f'По вертикали. Старт в столбце: {maxlen_col_index}, строка: {maxlen_col_start}, длина: {maxlen_col_len}')
print(f'Главная диагональ. Старт в строке: {maxlen_diag_main_start}, длина: {maxlen_diag_main_len}')
print(f'Побочная диагональ. Старт в столбце: {maxlen_diag_secondary_start}, длина: {maxlen_diag_secondary_len}')

# 6
rows = int(input())
columns = int(input())
a = []
for _ in range(rows):
    row = input().split()
    current_row = []
    for x in row:
        current_row.append(int(x))
    a.append(current_row)

result_row = 0
result_col = 0
result_len = 0
for i in range(rows):
    for j in range(columns):
        for l in range(1, columns - j + 1):
            found = True
            if i + l > rows:
                continue
            for x in range(i, i + l):
                for y in range(j, j + l):
                    if a[x][y] == 1:
                        found = False
            if found and l > result_len:
                result_len = l
                result_row = i
                result_col = j
if result_len == 0:
    print('Не найдено')
else:
    print(f'Строка: {result_row}, столбец: {result_col}, длина стороны: {result_len}')

# 7
list_1 = input().split()
list_2 = input().split()
a = []
b = []
for x in list_1:
    a.append(int(x))
for x in list_2:
    b.append(int(x))
n = len(a)
m = len(b)
found = False
for i in range(n - 1):
    for j in range(i + 1, n):
        sum_a = a[i] + a[j]
        for x in range(m - 2):
            for y in range(x + 1, m - 1):
                for z in range(y + 1, m):
                    sum_b = b[x] + b[y] + b[z]
                    if sum_a == sum_b:
                        found = True
if found:
    print('YES')
else:
    print('NO')

# 8
list_1 = input().split()
a = []
for x in list_1:
    a.append(int(x))
max_value = a[0]
max_count = a.count(max_value)
for x in a:
    current_count = a.count(x)
    if max_count < current_count:
        max_count = current_count
        max_value = x
print(max_value)

