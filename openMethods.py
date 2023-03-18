# Replace the f and df return by the function

def f(x):
    return -9.6*pow(x, 5)-12*pow(x, 3)+10  # -1.6*pow(x, 6)-3*pow(x, 4)+10*x


def df(x):
    return -48*pow(x, 4)-36*pow(x, 2)


def d2f(x):
    return -192*pow(x, 3)-72*x


def nr(x0, eps, p=1.0):
    tab_v = []
    tab_i = []
    x = x0
    i = 0
    while abs(f(x)) > eps:
        x = x - p*(f(x)/df(x))
        i += 1
        tab_v.append(x)
        tab_i.append(i)
    return tab_v, tab_i


def hly(x0, eps=0.000000001):
    tab_v = []
    tab_i = []
    x = x0
    i = 0
    while abs(f(x)) > eps:
        x = x - (2*f(x)*df(x))/(2*pow(df(x), 2)-f(x)*d2f(x))
        i += 1
        tab_v.append(x)
        tab_i.append(i)
    return tab_v, tab_i


def sct(min, max, eps=0.0001, p=1):
    tab_v = []
    tab_i = []
    for i in range(50):
        pente = (f(max)-f(min))/(max-min)
        max_sup = max - p*(f(max)/pente)
        if abs(max_sup - max) < eps:
            tab_i.append(i)
            tab_v.append(max_sup)
            return tab_v, tab_i

        tab_i.append(i)
        tab_v.append(max_sup)
        min = max
        max = max_sup

    return None


# print(nr(2, 0.000000001))
# print(sct(0, 4, 0.000000001))
# print(hly(1))
