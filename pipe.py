"""module docstring"""

def zero(starting_point):
    """func docstring"""
    return starting_point ** 2


def one(starting_point):
    """func docstring"""
    return starting_point // 2


def two(starting_point):
    """func docstring"""
    return starting_point + 4


def calc(starting_point, *func_order):
    """func docstring"""
    order = func_order
    result = starting_point
    functions = [zero, one, two]
    for item in order:
        result = functions[item](result)

    return result
