import pytest
from comma import comma_join


def test_empty_list():
    arg = []
    assert comma_join(arg) is None


def test_1_item():
    arg = ["One"]
    assert comma_join(arg) == "One"


def test_2_items():
    arg = ["One", "Two"]
    assert comma_join(arg) == "One and Two"


def test_3_items():
    arg = ["One", "Two", "Three"]
    assert comma_join(arg) == "One, Two and Three"


def test_4_items():
    arg = ["One", "Two", "Three", "Four"]
    assert comma_join(arg) == "One, Two, Three, and Four"
