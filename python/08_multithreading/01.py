import threading


class ThreadSafeCounter:

    def __init__(self, start, stop, value=None):
        self._start = start
        self._stop = stop
        self._value = value
        self._lock = threading.Lock()
        if self._value is None:
            self._value = self._start

    def inc(self):
        with self._lock:
            if self._value + 1 < self._stop:
                self._value += 1
            else:
                print('Maximum value reached')

    def dec(self):
        with self._lock:
            if self._value - 1 >= self._start:
                self._value -= 1
            else:
                print('Minimum value reached')

    @property
    def value(self):
        with self._lock:
            return self._value


def test(c: ThreadSafeCounter):
    c.inc()
    c.inc()
    c.dec()


counter = ThreadSafeCounter(0, 200)

threads = []
for _ in range(100):
    t = threading.Thread(target=test, args=(counter,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter.value)

