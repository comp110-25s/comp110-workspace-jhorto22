"""File to define Bear class."""


class Bear:

    def __init__(self):
        """Initializing Bear age and hunger score"""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """One day for the bear"""
        self.age += 1
        self.hunger_score -= 1
        return self.age

    def eat(self, num_fish: int) -> None:
        """Bear eating the fish"""
        self.hunger_score += num_fish
