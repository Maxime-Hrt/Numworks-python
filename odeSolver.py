import math


# Pour une equa diff du type y'+5y=0
# avec y(0)=1, on a y=y0*exp(-5x)
def f_diff(x, y):  # Equation differentielle:
    return -y+math.exp(-x)


def eu(h, nb_points, y_init):
    tab_coord = []
    y = y_init
    tab_coord.append((0, y_init))

    for i in range(1, nb_points):
        tab_coord.append((i*h, y+h*f_diff(i*h, y)))
        y = y+h*f_diff(i*h, y)
    return tab_coord


def rk2(h, nb_points, y_init):  # Runge-Kutta 2
    tab_coord = []
    y = y_init
    tab_coord.append((0, y_init))

    # i*h = x ; pour beta = 1/2
    for i in range(1, nb_points):
        k1 = f_diff(i*h, y)
        k2 = f_diff(i*h+h, y+h*k1)
        y = y + h*(k1+k2)/2
        # si beta = 1
        # k2 = f_diff(i*h+h/2, y+(h*k1)/2)
        # y = y + h*k2
        tab_coord.append((i*h, y))
    return tab_coord


def rk4(h, nb_points, y_init):  # Runge-Kutta 4
    tab_coord = []
    y = y_init
    tab_coord.append((0, y_init))

    for i in range(1, nb_points):
        k1 = f_diff(i*h, y)
        k2 = f_diff(i*h+h/2, y+(h*k1)/2)
        k3 = f_diff(i*h+h/2, y+(h*k2)/2)
        k4 = f_diff(i*h+h, y+h*k3)
        y = y + h*(k1+2*k2+2*k3+k4)/6
        tab_coord.append((i*h, y))
    return tab_coord

# print(eu(.01, 1000, 1))
# print(rk2(.01, 1000, 1))
# print(rk4(.01, 1000, 1))
