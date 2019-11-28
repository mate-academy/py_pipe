"""
Calculate the result of composition of functions
"""


def calc(num: float, *funcs: int) -> float:
    """Calculate"""
    functions = {
        0: lambda x: x * x,
        1: lambda x: x // 2,
        2: lambda x: x + 4,
    }

    result = num

    for func in funcs:
        result = functions[func](result)

    return result
