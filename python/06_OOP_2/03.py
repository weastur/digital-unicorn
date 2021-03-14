class OutOfBoundsError(Exception):

    def __init__(self, start, stop, current, *args, **kwargs):
        self._start = start
        self._stop = stop
        self._current = current

    def __str__(self):
        return f"Counter({self._start} - {self._stop}) out of bounds: current - {self._current}"


class Counter:

    def __init__(self, start, stop, value=None):
        self._start = start
        self._stop = stop
        self.value = value
        if self.value is None:
            self.value = self._start

    def inc(self):
        if self.value + 1 < self._stop:
            self.value += 1
        else:
            raise OutOfBoundsError(self._start, self._stop, self.value)

    def dec(self):
        if self.value - 1 >= self._start:
            self.value -= 1
        else:
            raise OutOfBoundsError(self._start, self._stop, self.value)


counter = Counter(1, 3, 1)
counter.inc()
print(counter.value)
try:
    counter.inc()
    print(counter.value)
except OutOfBoundsError as err:
    print(err)
counter.dec()
print(counter.value)
