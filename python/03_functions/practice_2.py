# 1

import functools


def cached(func):

    cache = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        # Для решения только с позиционными агрументами достаточно str(sorted(args))
        key = str(sorted(args)) + str(sorted(kwargs.items(), key=lambda item: (str(item[0]), str(item[1]))))
        if key not in cache:
            print('Calc and store to cache')
            cache[key] = func(*args, **kwargs)
        else:
            print('Already in cache')
        return cache[key]

    return inner


@cached
def foo(x, y):
    return x + y


print(foo(2, 2))
print(foo(2, 3))
print(foo(3, 2))
print(foo(2, 2))


# 2

import functools
import time


def cached(timeout=1):

    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = str(sorted(args)) + str(sorted(kwargs.items(), key=lambda item: (str(item[0]), str(item[1]))))
            now = time.time()
            if key not in cache or now - cache[key][0] > timeout:
                print('Calc and store to cache')
                cache[key] = now, func(*args, **kwargs)
            else:
                print('Already in cache')
            return cache[key][1]

        return inner
    return decorator


@cached(timeout=2)
def foo(x, y):
    return x + y


print(foo(2, 2))
print(foo(2, 3))
time.sleep(1)
print(foo(3, 2))
print(foo(2, 2))
time.sleep(1)
print(foo(3, 2))
print(foo(2, 2))