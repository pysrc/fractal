# 窗花
from fractal import Pen

p = Pen([500, 500], title="Window")
p.setPoint([495, 495])
p.setAngle(90)
p.doD0L(omega="f+f+f+f", P={"f": "ff+f--f+f"},
        delta=90, times=5, length=490, rate=3)
p.wait()
