"""docstring"""


def calc(val: float, *_funcs: int) -> float:
    """calc"""
    def zero(inp):
        return inp * inp

    def first(inp):
        return inp // 2

    def second(inp):
        return inp + 4

    for i in locals()["_funcs"]:
        if i == 2:
            val = second(val)
        elif i == 1:
            val = first(val)
        elif i == 0:
            val = zero(val)
    return val
