# Sier三角变换
from fractal import IFS
from random import randint


def ifsp(x, y):
    p = randint(1, 3)
    if p == 1:
        return (0.5 * x, 0.5 * y)
    elif p == 2:
        return (0.5 * x + 0.5, 0.5 * y + 0.5)
    else:
        return (0.5 * x + 0.5, 0.5 * y)

ob = IFS([460, 450], title="Sier")
ob.setPx(400, 0, 10)
ob.ifsp = ifsp
ob.doIFS(200000)
ob.wait()
