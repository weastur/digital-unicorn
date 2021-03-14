from branch import Branch


class Order:
    """
    Класс заказа

    Храним откуда и куда необходима доставка. Вес груза. Желаемые стоимость, время.
    """

    def __init__(self, branch_a: Branch, branch_b: Branch, weight, desired_cost, desired_time):
        self.branch_a = branch_a
        self.branch_b = branch_b
        self.weight = weight
        self.desired_cost = desired_cost
        self.desired_time = desired_time

    def __str__(self):
        return f'Order from {self.branch_a} to {self.branch_b}'
