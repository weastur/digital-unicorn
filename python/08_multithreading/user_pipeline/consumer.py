import time
from queue import Queue
from profile import UserProfile, UserStorage
from exceptions import ValidationError
from constants import RAW_USER_CONSUMER_SLEEP_TIME, USER_CONSUMER_SLEEP_TIME


def consume_raw_user(incoming: Queue, outgoing: Queue):
    while True:
        print("Incoming queue size", incoming.qsize())
        print("Outgoing queue size", outgoing.qsize())
        raw_user = incoming.get()
        print("Get raw user from queue", raw_user)
        try:
            outgoing.put(UserProfile(**raw_user))
        except ValidationError as err:
            print("Cannot create user profile", err)
        else:
            print("Successfully putted user profile to queue")
        finally:
           time.sleep(RAW_USER_CONSUMER_SLEEP_TIME)


def consume_user_profile(q: Queue, storage: UserStorage):
    while True:
        user = q.get()
        storage.add(user)
        time.sleep(USER_CONSUMER_SLEEP_TIME)
