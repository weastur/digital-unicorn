# 1
def bin_search(a, x):
    l, r = 0, len(a)
    while r - l > 1:
        m = l + (r - l) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    if l < len(a) and a[l] == x:
        return True
    return False


a = list(map(int, input().split()))
x = int(input())
if bin_search(a, x):
    print('YES')
else:
    print('NO')

# 2
def calc(x):
    if x == 0:
        return 0
    else:
        return x % 10 + calc(x // 10)


n = int(input())
print(calc(n))

3
def decorator(func):

    def inner(s):
        if len(s) % 2 == 1:
            s = '1_' + s
        else:
            s = '0_' + s
        func(s)

    return inner


@decorator
def foo(s):
    print(s)


s = input()
foo(s)

# 4
def rec(a, b):
    if a < b:
        print(a, end=' ')
        rec(a + 1, b)
    elif a > b:
        print(a, end=' ')
        rec(a - 1, b)
    else:
        print(a)


a = int(input())
b = int(input())
rec(a, b)

# 5

def check(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return check(n // 2)
    else:
        return False


n = int(input())
if check(n):
    print('YES')
else:
    print('NO')

# 6
def flip(func):

    def inner(*args, **kwargs):
        return func(*tuple(reversed(args)), **kwargs)

    return inner


@flip
def div(x, y, show=False):
    res = x // y
    if show:
        print(res)
    return res


div(2, 4, show=True)

















