from branch import Branch


class BaseTransport:
    """
    Базовый класс для всех видов транспорта

    Общим для всех объектов будут стоимость за кг, скорость, вероятность аварии на обычной и скоростной дороге
    """

    def __init__(self, cost, speed, accident_prob, speed_routes_accident_prob):
        self.cost = cost
        self.speed = speed
        self.accident_prob = accident_prob
        self.speed_routes_accident_prob = speed_routes_accident_prob

    @staticmethod
    def match(branch_a: Branch, branch_b: Branch):
        """Вернет True если доставка между филиалами возможна."""
        raise NotImplementedError


class Avia(BaseTransport):

    @staticmethod
    def match(branch_a: Branch, branch_b: Branch):
        """Вернет True если погода в городах хорошая и города являются большими."""
        return (
                branch_a.is_good_weather() and branch_b.is_good_weather() and
                branch_a.is_big() and branch_b.is_big()
        )

    def __str__(self):
        return 'Avia'


class Railway(BaseTransport):

    @staticmethod
    def match(branch_a: Branch, branch_b: Branch):
        """Вернет True если города как минимум средние по размеру."""
        return branch_a.is_middle() and branch_b.is_middle()

    def __str__(self):
        return 'Railway'


class Auto(BaseTransport):

    @staticmethod
    def match(branch_a: Branch, branch_b: Branch):
        """По условиям задачи всегда True."""
        return True

    def __str__(self):
        return 'Auto'
