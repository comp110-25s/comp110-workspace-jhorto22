__author__: str = "730759854"


def invert(switch: dict[str, str]) -> dict[str, str]:
    """Inverting key and values"""
    inverted = {}
    for key in switch:
        value = switch[key]
        if value in inverted:
            raise KeyError(f"Duplicate value found: {value}")
        inverted[value] = key
    return inverted


def count(appears: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in input list"""
    amount = {}
    for item in appears:
        if item in amount:
            amount[item] += 1
        else:
            amount[item] = 1
    return amount


def favorite_color(color: dict[str, str]) -> str:
    """Finding the color that appears most frequently"""
    frequency = {}
    most_frequent = ""
    max = 0

    for key in color:
        favorite_color = color[key]
        if favorite_color in frequency:
            frequency[favorite_color] += 1
        else:
            frequency[favorite_color] = 1
        if frequency[favorite_color] > max:
            most_frequent = favorite_color
            max = frequency[favorite_color]
    return most_frequent


def bin_len(trash: list[str]) -> dict[int, set[str]]:
    """Trashes a group of strings by length"""
    bins: dict[int, set[str]] = {}
    group_elements = ""

    for group_elements in trash:
        length = len(group_elements)
        if length not in bins:
            bins[length] = set()
        bins[length].add(group_elements)
    return bins
