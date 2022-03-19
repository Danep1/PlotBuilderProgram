import numpy as np
from math import cos, sin, tan, sqrt, acos, asin, atan, log
from sympy import Symbol, solve, diff
from main.modern_func import modern_func

y_data = np.array([], float)
x_data = np.array([], float)


def root(i, x):
    '''Функция нахождения i-го корня из x'''
    if i != int(i):
        raise ArithmeticError
    if i % 2 == 0:
        if x < 0:
            raise ArithmeticError
        return x ** (1 / i)
    else:
        if x < 0:
            return - ((-x) ** (1 / i))
        else:
            return x ** (1 / i)


def func_existing(text_func, x):
    try:
        y = eval(text_func)
    except ValueError:
        return False
    except ArithmeticError:
        return False
    finally:
        return True


def func(text_func, interval, step):
    for x in np.arange(interval, step):
        if func_existing(text_func, x):

    analis = ''


if __name__ == '__main__':
    pass
