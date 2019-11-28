"""pipe module"""


def function0(num):
    """
    :param num:
    :return:
    """
    return num * num


def function1(num):
    """
    :param num:
    :return:
    """
    return num // 2


def function2(num):
    """
    :param num:
    :return:
    """
    return num + 4


def calc(num: float, *funcs: int) -> float:
    """
    :param num:
    :param funcs:
    :return:
    """
    functions = (function0, function1, function2)
    result = num
    for item in funcs:
        result = functions[item](result)
    return result
