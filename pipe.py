"""
module pipe
"""


def calc(num: float, *funcs: int) -> float:
    """
    You have three functions:
    f0: x*x
    f1: x//2
    f2: x + 4

    For given x and sequence of functions numbers calculate
    the result of composition of this functions.
    Example: (0, 1, 2) -> x = f2(f1(f0(x)))
    :param num: float
    :param funcs: int
    :return: float
    """
    func_dict = (
        lambda x: x * x,
        lambda x: x // 2,
        lambda x: x + 4
    )

    result_num = num
    for _, func in enumerate(funcs):
        result_num = func_dict[func](result_num)
    return result_num
