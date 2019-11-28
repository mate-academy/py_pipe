"""
docstring
"""


def calc(arg: float, *funcs: int) -> float:
    """

    :param x:
    :param funcs:
    :return:
    """
    func = {0: lambda x: x * x, 1: lambda x: x // 2, 2: lambda x: x + 4}
    result = arg
    for fun in funcs:
        result = func[fun](result)
    return result
