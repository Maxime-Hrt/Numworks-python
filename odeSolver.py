import math


def f_euler(x, y):
    return -y+math.exp(-x)


def euler_resolution(h, y, x):
    return y+h*f_euler(x, y)


def eu(h, nb_points, y_init):
    tab_coord = []
    y = y_init
    tab_coord.append(f"(0, {y_init})")

    for i in range(1, nb_points):
        tab_coord.append(f"({i*h}, {euler_resolution(h, y, i*h)})")
        y = euler_resolution(h, y, i*h)
    return tab_coord


# print(eu(.01, 1000, 1))
