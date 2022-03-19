import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, tan, sqrt, acos, asin, atan, log

dick = {'tg': 'tan', 'arccos': 'acos', 'arcsin': 'asin', 'arctan': 'atan', 'ln(': 'log(e,', 'lg(': 'log(10,', '^': '**'}


def modern_func(text_func):
    for i in dick.keys():
        text_func = text_func.replace(i, dick[i])
    return text_func[text_func.index('=') + 1:].strip()


def dispay_graf(text_func, interval=(10, 10), step=0.01):
    max_x, min_x = interval
    text_func = modern_func(text_func)

    data_y = np.arange(min_x, max_x, step)
    data_x = np.array(list(map(lambda x: eval(text_func), data_y)))
    fig, ax = plt.subplots()

    ax.set(xlabel='x', ylabel='y')  # Задаем оси координат
    ax.plot(interval, interval,
            scalex=True, scaley=True, color='w', linewidth=0.001)
    ax.plot(interval, [0, 0], linewidth=2., color='black', scalex=False, scaley=False)
    ax.plot([0, 0], interval, linewidth=2., color='black', scalex=False, scaley=False)

    plt.grid(True, linestyle='--')  # Вспомогательные линии

    ax.plot(data_y, data_x, scalex=False, scaley=False)  # Строим график функции

    plt.show()


if __name__ == '__main__':
    pass