# 树形
from fractal import Pen

p = Pen([260, 500])

p.setPoint([130, 500])

p.setAngle(90)

p.doD0L(omega="f", P={"f": "f[-f]f[+f]f"},
        delta=30, times=5, length=480, rate=3)

p.save("tree.jpg")

p.wait()
