import pipe


def test_square():
    assert pipe.calc(1, 0) == 1


def test_012():
    assert pipe.calc(1, 0, 1, 2) == 4


def test_210():
    assert pipe.calc(1, 2, 1, 0) == 4


def test_222():
    assert pipe.calc(1, 2, 2, 2) == 12