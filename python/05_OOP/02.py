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
            print('Maximum value reached')

    def dec(self):
        if self.value - 1 >= self._start:
            self.value -= 1
        else:
            print('Minimum value reached')


counter = Counter(1, 3, 2)
counter.inc()
print(counter.value)
counter.inc()
print(counter.value)
counter.dec()
print(counter.value)