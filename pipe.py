"""docstring"""

def calc(number: float, *funcs: int) -> float:
    """use tuple of lambda function for calculate"""
    func = (
        lambda x: x * x,
        lambda x: x // 2,
        lambda x: x + 4
    )
    res = number
    for i in funcs:
        res = func[i](res)
    return res
