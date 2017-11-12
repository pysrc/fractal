# 谢尔宾斯基方毯

from fractal import Pen

p = Pen([500, 500], title="Sierpinski")
p.setPoint([50, 240])
p.doD0L(omega="f", P={"h": "hhh", "f": "f-f+f+f+h-f-f-f+f"},
        delta=90, times=4, length=400, rate=3)
p.wait()
