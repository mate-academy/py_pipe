'''
Module
'''


def first_function(number):
    '''

    :param x:
    :return:
    '''
    return number * number


def second_function(number):
    '''

    :param x:
    :return:
    '''
    return number // 2


def third_function(number):
    '''

    :param x:
    :return:
    '''
    return number + 4


def calc(number: float, *funcs: int) -> float:
    '''

    :param number:
    :param funcs:
    :return:
    '''
    dictionary = {0: first_function, 1: second_function, 2: third_function}
    result = number
    for i in funcs:
        result = dictionary[i](result)
    return result
