import threading


class ThreadSafeStorage:

    def __init__(self, *args):
        self._values = list(args)
        self._lock = threading.Lock()

    def add(self, value):
        with self._lock:
            self._values.append(value)

    def remove(self, value):
        with self._lock:
            self._values.remove(value)

    def find(self, value):
        with self._lock:
            return self._values.index(value)

    def print_all(self):
        with self._lock:
            print(self._values)


def test(s: ThreadSafeStorage):
    s.add(42)
    s.remove(42)


storage = ThreadSafeStorage(1, 2, 3, 4, 5)

threads = []
for _ in range(100):
    t = threading.Thread(target=test, args=(storage,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

storage.print_all()