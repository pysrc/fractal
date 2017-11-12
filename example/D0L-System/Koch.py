# 科赫曲线
from fractal import Pen

p = Pen([500, 300], title="Koch")
p.setPoint([5, 190])
p.doD0L(omega="f", P={"f": "f+f--f+f"}, delta=60, times=4, length=490, rate=3)
p.wait()
