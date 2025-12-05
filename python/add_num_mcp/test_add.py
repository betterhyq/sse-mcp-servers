from pytest import fixture

from . import add_tool


@fixture
def add():
    return add_tool.add


def test_add(add):
    assert add(1, 2) == "3"
    assert add(1, -2) == "-1"
    assert add(1, 0) == "1"
    assert add(1, 1) == "2"
    assert add(1, 2) == "3"
    assert add(1, 2) == "3"
