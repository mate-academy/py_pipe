"""
docstring
"""
import pipe


def test_square():
    """

    :return:
    """
    assert pipe.calc(1, 0) == 1


def test_012():
    """

    :return:
    """
    assert pipe.calc(1, 0, 1, 2) == 4


def test_210():
    """

    :return:
    """
    assert pipe.calc(1, 2, 1, 0) == 4


def test_222():
    """

    :return:
    """
    assert pipe.calc(0, 2, 2, 2) == 12
