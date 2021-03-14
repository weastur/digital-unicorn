class Range:

    def __init__(self, start, stop=None, step=1):
        if stop is not None:
            self._start = start
            self._stop = stop
        else:
            self._start = 0
            self._stop = start
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        result = self._start
        if (result >= self._stop and self._step > 0) or (result <= self._stop and self._step < 0):
            raise StopIteration
        self._start += self._step
        return result


for i in Range(10, 0, -2):
    print(i)
print('='*20)
for i in Range(2, 5):
    print(i)
print('='*20)
for i in Range(4):
    print(i)
