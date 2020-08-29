# 1

def rec(n):
    if n > 0:
        rec(n - 1)
        print(n, end=' ')


rec(10)

# 2
import functools
import time


def benchmark(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print('Time elapsed:', time.time() - start_time)
        return result

    return inner


@benchmark
def foo(x, y):
    return x + y


foo(1, 2)

# 3
import functools
import time


def benchmark(iters_count=1):

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            total_time = 0
            result = None
            for _ in range(iters_count):
                start_time = time.time()
                result = func(*args, **kwargs)
                total_time += time.time() - start_time
            print('Average time elapsed:', total_time / iters_count)
            return result

        return inner
    return decorator


@benchmark(iters_count=10)
def foo(x, y):
    return x + y


foo(1, 2)
