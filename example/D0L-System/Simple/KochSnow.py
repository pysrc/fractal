# 科赫雪花
from fractal import Pen

p = Pen([500,500],title = "Koch Snow")

p.setPoint([30,130])

p.doD0L(omega = "f--f--f", P = {"f": "f+f--f+f"}, delta = 60, times = 5, length = 400, rate = 3)

p.wait()