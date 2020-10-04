import random
import string


def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def random_number(length=8):
    return ''.join(random.choice(string.digits) for _ in range(length))


def random_password(min_length=8, max_length=15):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.printable) for _ in range(length))
