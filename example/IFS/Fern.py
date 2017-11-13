# 蕨类IFS生成

from fractal import IFS
from random import random


def ifsp(x, y):
    p = random()
    if p < 0.01:
        return (0, 0.16 * y)
    elif p < 0.07:
        if random() > 0.5:
            return (0.21 * x - 0.25 * y, 0.25 * x + 0.21 * y + 0.44)
        else:
            return (-0.2 * x + 0.26 * y, 0.23 * x + 0.22 * y + 0.6)
    else:
        return (0.85 * x + 0.1 * y, -0.05 * x + 0.85 * y + 0.6)

ob = IFS([400, 500], title = "蕨")
ob.setPx(100, 100, 100)
ob.ifsp = ifsp
ob.doIFS(200000)
ob.wait()