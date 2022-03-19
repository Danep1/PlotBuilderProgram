import matplotlib.pyplot as plt


def dispay_graf(data_x, data_y, interval):
    max_x, min_x = interval
    # text_func = modern_func(text_func)

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
