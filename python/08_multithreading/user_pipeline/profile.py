import hashlib
import re

from threading import Lock

from exceptions import FullNameError, EmailError, PasswordError, PhoneError


class UserProfile:

    FULL_NAME_REGEX = re.compile(r"^[\w\s]{1,255}$")
    PHONE_REGEX = re.compile(r"^\+\d+$")
    EMAIL_REGEX = re.compile(r"^\w+@\w+\.\w+$")

    def __init__(self, full_name, email, phone, password):
        self._full_name = full_name
        self._email = email
        self._phone = phone
        self._password = self._hash_password(password)
        self._validate_all()

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).digest()

    def _validate_all(self):
        self._validate_full_name(self._full_name)
        self._validate_email(self._email)
        self._validate_phone(self._phone)

    def _validate_length(self, value, length=255):
        if len(value) > length:
            return False
        return True

    def _validate_full_name(self, value):
        if not self.FULL_NAME_REGEX.match(value):
            raise FullNameError("Invalid full name")

    def _validate_email(self, value):
        if not self.EMAIL_REGEX.match(value):
            raise EmailError("Invalid format")

    def _validate_phone(self, value):
        if not self.PHONE_REGEX.match(value):
            raise PhoneError("Invalid format")

    def _validate_password(self, value: str):
        if len(value) < 10:
            raise PasswordError("Too short password")
        upper, lower, digit = False, False, False
        for char in value:
            upper = upper or char.isupper()
            lower = lower or char.islower()
            digit = digit or char.isdigit()
        if not all((upper, lower, digit)):
            raise PasswordError("Invalid password")

    @property
    def full_name(self):
        return self._full_name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    @property
    def password(self):
        return self._password

    @full_name.setter
    def full_name(self, value):
        self._validate_full_name(value)
        self._full_name = value

    @email.setter
    def email(self, value):
        self._validate_email(value)
        self._email = value

    @phone.setter
    def phone(self, value):
        self._validate_phone(value)
        self._phone = value

    @password.setter
    def password(self, value):
        self._validate_password(value)
        self._password = self._hash_password(value)

    def check_password(self, value):
        return self._password == self._hash_password(value)

    def info(self):
        return {
            "full_name": self._full_name,
            "email": self._email,
            "phone": self._phone,
        }


class UserIterator:

    def __init__(self, users: list, lock: Lock):
        self._users = users
        self._lock = lock
        self._current_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        with self._lock:
            if self._current_pos == len(self._users):
                raise StopIteration
            self._current_pos += 1
            return self._users[self._current_pos - 1]


class UserStorage:

    def __init__(self):
        self._users = []
        self._lock = Lock()

    def add(self, user: UserProfile):
        with self._lock:
            self._users.append(user)

    def remove(self, user: UserProfile):
        with self._lock:
            self._users.remove(user)

    def all(self):
        return UserIterator(self._users, self._lock)
