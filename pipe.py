"""docstring"""


def calc(value: float, *funcs: int) -> float:
    """calculate the result of composition of this functions"""
    funcs_list = [lambda inp: inp * inp, lambda inp: inp // 2, lambda inp: inp + 4]
    for i in funcs:
        value = funcs_list[i](value)
    return value
