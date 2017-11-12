# 其他曲线
from fractal import Pen

p = Pen([500, 500], title="Else")
p.setPoint([250, 250])
p.doD0L(omega="f+f+f+f", P={"f": "ff-f-f-f-f+f-f"},
        delta=90, times=5, length=100, rate=3)
p.wait()
