# 谢尔宾斯基三角

from fractal import Pen

p = Pen([500, 460], title="Sierpinski")
p.setPoint([5, 5])
p.doD0L(omega="f--f--f", P={"g": "gg", "f": "f--f--f--gg"},
        delta=60, times=5, length=490, rate=2)
p.wait()
