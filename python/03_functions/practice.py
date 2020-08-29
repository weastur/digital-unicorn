# 1

def foo(x, y):
    return x + y

# 2

def foo(x, y, *args):
    return (x + y + sum(args)) / (2 + len(args))


print(foo(1, 2, 3, 4, 5))

# 3

def uniq(s):
    return len(set(s))


print(uniq('abcabcd'))

# 4

def create_dict(**kwargs):
    result = {}
    for key in kwargs:
        result[kwargs[key]] = len(kwargs[key])
    return result


print(create_dict(arg1='first_key', arg2='second_key'))

# 5

def get_data():
    first_name = input()
    last_name = input()
    age = int(input())
    return (first_name, last_name, age)

# 6

def swap(a):
    max_index = a.index(max(a))
    min_index = a.index(min(a))
    b = a.copy()
    b[max_index], b[min_index] = b[min_index], b[max_index]
    return b


print(swap([1, 2, 3, 4, 5]))

# 7

def non_uniq(a):
    result = []
    for x in a:
        if a.count(x) > 1 and x not in result:
            result.append(x)
    return result


print(non_uniq([1, 2, 2, 3, 1]))