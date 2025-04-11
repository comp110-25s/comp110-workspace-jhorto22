"""Identifying the resources  required for a tea party"""

__author__: str = "730759854"


def main_planner(guests: int) -> None:
    """Bringing tea bags, treats and costs together"""
    print(" A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Number of tea bags needed for party"""
    return 2 * people
    print(2 * people)


def treats(people: int) -> int:
    """Treats needed for party"""
    return tea_bags(people) * 3 // 2


def cost(tea_count: int, treat_count: int) -> float:
    """What is the cost for tea and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    # main_planner(guests=int(input("How many guests are attending your tea party? ")))
    main_planner(guests=4)
