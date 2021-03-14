import random
import time

import constants
from agency import Agency
from order import Order


def main():
    agency = Agency()  # Создаем агенство
    while True:
        branch_a, branch_b = None, None  # Случайным образом выбираем два филиала
        while branch_a == branch_b:
            branch_a, branch_b = random.choices(agency.branches, k=2)
        order = Order(  # Случайным образом создаем объект заказа
            branch_a=branch_a,
            branch_b=branch_b,
            weight=random.randint(1, constants.MAX_WEIGHT),
            desired_cost=random.randint(1, constants.MAX_DESIRED_COST),
            desired_time=random.randint(1, constants.MAX_DESIRED_TIME),
        )
        agency.process_order(order)  # Обрабатываем
        agency.print_stats()  # Печатаем статистику
        time.sleep(constants.SLEEP_TIME_SEC)  # Засыпаем на время


if __name__ == '__main__':
    main()
