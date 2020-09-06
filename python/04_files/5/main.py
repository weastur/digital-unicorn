from file_utils import count

from math_utils import factorial
from math_utils import primes

task_number = int(input("Введите номер задачи для решения: "))

if task_number == 1:
    n = int(input("Введите число: "))
    print(factorial.calc_factorial(n))
elif task_number == 2:
    n = int(input("Введите число: "))
    print(primes.is_prime(n))
elif task_number == 3:
    file_name = input("Путь к файлу: ")
    print(count(file_name))