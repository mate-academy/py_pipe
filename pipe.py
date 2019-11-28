"""docstring"""


def calc(arg: float, *funcs: int) -> float:
    """

    :param arg: float
    :param funcs: int
    :return: float
    """
    functions = {
        0: lambda x: x * x,
        1: lambda x: x // 2,
        2: lambda x: x + 4}

    res = arg
    for func in funcs:
        res = functions[func](res)
    return res
