"""docstring"""


def calc(x: float, *funcs: int) -> float:
    """calc"""
    for i in locals()["funcs"]:
        if i == 2:
            a = lambda x: x + 4
            x = a(x)
        elif i == 1:
            b = lambda x: x// 2
            x = b(x)
        elif i == 0:
            c = lambda x: x * x
            x = c(x)

    print(x)
    return x


calc(0, 2, 2, 2)
