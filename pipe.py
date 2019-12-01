"""
func0, func1, func2, calc
"""


def func0(num):
    """

    :param num:
    :return:
    """
    return num * num


def func1(num):
    """

    :param num:
    :return:
    """
    return num // 2


def func2(num):
    """

    :param num:
    :return:
    """
    return num + 4


def calc(number: float, *funcs: int) -> float:
    """

    :param number:
    :param funcs:
    :return:
    """
    func_list = {
        0: func0,
        1: func1,
        2: func2,
    }

    res = number
    for item in funcs:
        res = func_list[item](res)
        print(res, item)

    return res
