import random
from collections import defaultdict

import constants
from branch import Branch
from order import Order
from transport import Avia, Railway, Auto


class Agency:

    def __init__(self):
        self.routes = defaultdict(dict)  # defaultdict -- полезная штука, почитайте в доке. Но по сути все равно словарь
        self.speed_routes = defaultdict(dict)
        self.avia = Avia(100, 500, 0.001, 0.0005)
        self.railway = Railway(10, 140, 0.01, 0.005)
        self.auto = Auto(1, 90, 0.1, 0.05)
        self.branches = []  # Список филиалов
        self.processed_orders = []  # Список обработанных заказов
        self.canceled_orders = []  # Список отменненных заказов
        self.accident_orders = []  # Список аварийных заказов
        self.damages = 0  # Потери
        self.profit = 0  # Прибыль
        # Генерируем филиалы
        for _id in range(random.randint(1, constants.MAX_BRANCH_COUNT)):
            self.branches.append(
                Branch(
                    name=f"branch_{_id}",
                    good_weather=random.choice((True, False)),
                    population=random.randint(constants.MIN_POPULATION, constants.MAX_POPULATION)
                )
            )
        # Генерируем маршруты. Маршруты храняться в словаре словарей. Ключами являются имена филиалов, а значением словаря
        # словарей является длина дороги
        for branch_a in self.branches:
            for branch_b in self.branches:
                if branch_a == branch_b:
                    continue
                self.routes[branch_a.name][branch_b.name] = random.randint(1, constants.MAX_DISTANCE)
                self.routes[branch_b.name][branch_a.name] = self.routes[branch_a.name][branch_b.name]
        # Генерируем скоростные маршруты. Не более десятой части от кол-ва филиалов
        for _ in range(len(self.branches) // 10):
            branch_a, branch_b = None, None
            while branch_a == branch_b:
                branch_a, branch_b = random.choices(self.branches, k=2)
            self.speed_routes[branch_a.name][branch_b.name] = self.routes[branch_a.name][branch_b.name]
            self.speed_routes[branch_b.name][branch_a.name] = self.speed_routes[branch_a.name][branch_b.name]

    def print_stats(self):
        print("=========================")
        print("Processed orders count:", len(self.processed_orders))
        print("Canceled orders count:", len(self.canceled_orders))
        print("Accident orders count:", len(self.accident_orders))
        print("Profit:", self.profit)
        print("Damages:", self.damages)
        print("=========================")

    def process_order(self, order: Order):
        found = False
        for transport in [self.avia, self.railway, self.auto]:  # Полиморфизм в действии
            if not transport.match(order.branch_a, order.branch_b):  # Вид транспорта не подошел
                continue
            # Если есть скоростной маршрут
            speed_factor = constants.SPEED_FACTOR if self.routes[order.branch_a.name].get(order.branch_b.name) else 1
            cost = transport.cost * self.routes[order.branch_a.name][order.branch_b.name] * order.weight
            time = self.routes[order.branch_a.name][order.branch_b.name] / transport.speed / speed_factor
            if cost <= order.desired_cost and time <= order.desired_time:  # Подходит по цене и скорости
                found = True
                accident_happend = \
                random.choices((True, False), (transport.accident_prob, 1 - transport.accident_prob))[0]
                if accident_happend:  # Случилась беда
                    self.accident_orders.append(order)
                    self.damages += cost * 2
                else:
                    self.processed_orders.append(order)
                    self.profit += cost
                if found:  # Нашли подходящий транспорт. Вывели сообщение, поиск прекратили.
                    print(
                        "{order} processed by: {transport}, used {route} route".format(
                            order=order,
                            transport=transport,
                            route="non-speed" if speed_factor == 1 else "speed",
                        ),
                    )
                    break
        if not found:  # Ничего нет -- в список отклоненных
            self.canceled_orders.append(order)
