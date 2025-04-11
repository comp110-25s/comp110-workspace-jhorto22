"""File to define Fish class."""


class Fish:

    def __init__(self):
        """Initializing Fish age"""
        self.age = 0
        return None

    def one_day(self):
        """One day for the bear"""
        self.age += 1
        return self.age
