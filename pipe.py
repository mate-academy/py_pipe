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
    func_order = [*func_order]
    result = starting_point
    for item in func_order:
        if item == 0:
            result = zero(result)
        elif item == 1:
            result = one(result)
        elif item == 2:
            result = two(result)
        else:
            raise ValueError

    return result
