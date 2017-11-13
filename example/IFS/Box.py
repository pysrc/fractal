# Box IFS
from fractal import IFS
from random import randint


def ifsp(x, y):
    p = randint(1, 5)
    if p == 1:
        return (x / 3, y / 3)
    elif p == 2:
        return (x / 3 + 2 / 3, y / 3)
    elif p == 3:
        return (x / 3 + 1 / 3, y / 3 + 1 / 3)
    elif p == 4:
        return (x / 3, y / 3 + 2 / 3)
    else:
        return (x / 3 + 2 / 3, y / 3 + 2 / 3)

ob = IFS([500, 500], title="Box")
ob.setPx(490, 5, 5)
ob.setIfsp(ifsp)
ob.doIFS(200000)
ob.wait()
