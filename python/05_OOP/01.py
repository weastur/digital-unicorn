class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def max(self):
        return max(self.a, self.b)

    def print(self):
        print(f"a = {self.a}, b = {self.b}")

    def change(self, a, b):
        self.a = a
        self.b = b