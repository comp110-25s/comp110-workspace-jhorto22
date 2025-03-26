__author__: str = "730759854"

import pytest
from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_edge_case():
    with pytest.raises(KeyError):
        my_dictionary = {"one": "two", "three": "two"}
        assert invert(my_dictionary)


def test_invert_use_case():
    my_dictionary = {"eggs": "cheese"}
    assert invert(my_dictionary) == {"cheese": "eggs"}


def test_invert_use_case2():
    my_dictionary = {"hot": "potato", "left": "leg"}
    assert invert(my_dictionary) == {"potato": "hot", "leg": "left"}


def test_count_edge_case():
    assert count(["red"]) == {"red": 1}


def test_count_use_case():
    assert count(["rain", "rain", "hail"]) == {"rain": 2, "hail": 1}


def test_count_use_case2():
    assert count(["front", "back", "front", "side", "back"]) == {
        "front": 2,
        "back": 2,
        "side": 1,
    }


def test_favorite_color_edge_case():
    assert favorite_color({}) == ""


def test_favorite_color_use_case():
    assert favorite_color({"apple": "red", "ocean": "blue", "sky": "blue"}) == "blue"


def test_favorite_color_use_case2():
    assert favorite_color({"box": "white"}) == "white"


def test_bin_len_edge_case():
    assert bin_len(["Rat", "Egg", "Hit"]) == {3: {"Rat", "Egg", "Hit"}}


def test_bin_len_use_case():
    assert bin_len(["Pet", "Back", "Story"]) == {3: {"Pet"}, 4: {"Back"}, 5: {"Story"}}


def test_bin_len_use_case2():
    assert bin_len(["Sun", "Kid", "Porch"]) == {3: {"Sun", "Kid"}, 5: {"Porch"}}
