def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    while start != stop:
        yield start
        start += step

for i in my_range(10, 0, -2):
    print(i)
print('='*20)
for i in my_range(2, 5):
    print(i)
print('='*20)
for i in my_range(4):
    print(i)
