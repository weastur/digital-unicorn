import random
import time
from multiprocessing import Process, Queue


def producer(q: Queue):
    while True:
        q.put(random.randint(1, 100))
        time.sleep(1)


def consumer(q: Queue):
    while True:
        value = q.get()
        print(value)


q = Queue()
p1 = Process(target=producer, args=(q,))
p2 = Process(target=consumer, args=(q,))

p1.start()
p2.start()

while True:
    pass

