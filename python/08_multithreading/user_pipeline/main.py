from profile import UserStorage
from queue import Queue
from threading import Thread
import itertools
from producer import produce
from consumer import consume_raw_user, consume_user_profile


storage = UserStorage()
incoming, outgoing = Queue(), Queue()

producers = []
for _ in range(10):
    t = Thread(target=produce, args=(incoming,))
    producers.append(t)
    t.start()

raw_users_consumers = []
for _ in range(2):
    t = Thread(target=consume_raw_user, args=(incoming, outgoing))
    raw_users_consumers.append(t)
    t.start()

users_consumers = []
for _ in range(4):
    t = Thread(target=consume_user_profile, args=(outgoing, storage))
    users_consumers.append(t)
    t.start()

for t in itertools.chain(producers, raw_users_consumers, users_consumers):
    t.join()