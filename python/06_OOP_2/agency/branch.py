class Branch:
    """
    Класс филила

    Храним имя, хорошая ли погода и большой ли город.
    """

    def __init__(self, name, good_weather, population):
        self.name = name
        self._good_weather = good_weather
        self._population = population

    def is_good_weather(self):
        return self._good_weather

    def is_big(self):
        return self._population >= 1000 * 1000

    def is_middle(self):
        return self._population >= 100 * 1000

    def __str__(self):
        return f'{self.name}'
