"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removing old fish and old bears from river"""
        alive_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                alive_fish.append(fish)
        self.fish = alive_fish

        alive_bear: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                alive_bear.append(bear)
        self.bears = alive_bear

    def bears_eating(self):
        """Bears Eating the fish"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Finding the starving bear"""
        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                living_bears.append(bear)
        self.bears = living_bears

    def repopulate_fish(self):
        """Fish reproduction in river"""
        amt_baby_fish = (len(self.fish) // 2) * 4
        new_fish = 0
        while new_fish < amt_baby_fish:
            self.fish.append(Fish())
            new_fish += 1

    def repopulate_bears(self):
        """Bear reproduction in river"""
        amt_baby_bears = len(self.bears) // 2
        baby_bears: int = 0
        while amt_baby_bears < baby_bears:
            self.bears.append(Bear())
            baby_bears += 1

    def view_river(self):
        """Status of the Bear and Fish Pop"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Looking at the river every day of the week"""
        days = 0
        while days < 7:
            self.one_river_day()
            days += 1
        return


def remove_fish(self, amount: int) -> None:
    """ "Removing the frontmost fish from the river"""
    for fish in self.fish:
        deleting_fish: int = 0
        amount = 0
        while deleting_fish < amount:
            self.fish.pop(deleting_fish)
            deleting_fish += 1
