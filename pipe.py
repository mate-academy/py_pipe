"""Pipe of functions
"""


def calc(num: float, *funcs: int) -> float:
    """
    three functions:
    f0: x*x
    f1: x//2
    f2: x + 4
    For given x and order of functions calculate the result of
    composition of this functions.
    Example:
    (0, 1, 2) -> x = f2(f1(f0(x)))
    :param num: int
    :param funcs: order of function
    :return: int
    """
    result = num

    tuple_of_func = (
        lambda x: x * x,
        lambda x: x // 2,
        lambda x: x + 4
    )

    for i in funcs:
        result = tuple_of_func[i](result)

    return result
