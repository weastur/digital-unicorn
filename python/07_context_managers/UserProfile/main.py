from exceptions import PasswordError, PhoneError, EmailError, FullNameError
from profile import UserProfile, UserStorage

user = UserProfile("John Doe", "johndoe@example.com", "+5555555", "password")
user_2 = UserProfile("Jane Doe", "janedoe@example.com", "+6666666", "Password1!")

try:
    user.full_name = 'x' * 256
except FullNameError as err:
    print(err)

try:
    user.email = 'x' * 256
except EmailError as err:
    print(err)

try:
    user.email = 'xxxx'
except EmailError as err:
    print(err)

try:
    user.password = 'trololo'
except PasswordError as err:
    print(err)

try:
    user.password = 'x' * 256
except PasswordError as err:
    print(err)

try:
    user.phone = '123'
except PhoneError as err:
    print(err)

storage = UserStorage()
storage.add(user)
storage.add(user_2)
storage.remove(user)

for u in storage.all():
    print(u.info())
