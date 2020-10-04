import time
import utils
from queue import Queue
from constants import PRODUCER_SLEEP_TIME


def produce(q: Queue):
    while True:
        q.put({
            "full_name": utils.random_string() + ' ' + utils.random_string(),
            "email": utils.random_string() + '@' + utils.random_string() + '.' + utils.random_string(),
            "phone": '+' + utils.random_number(),
            "password": utils.random_password(),
        })
        time.sleep(PRODUCER_SLEEP_TIME)
