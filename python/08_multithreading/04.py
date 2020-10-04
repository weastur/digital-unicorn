from itertools import zip_longest
from multiprocessing import Pool


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def get_max(*args):
    return max(map(int, *args))


with open('input.txt') as in_file:
    lines = in_file.readlines()
    with Pool(5) as pool:
        chunks = grouper(lines, (len(lines) + 4) // 5, 0)
        print(max(pool.map(get_max, chunks)))
