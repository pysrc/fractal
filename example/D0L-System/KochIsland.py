# 二次Koch岛
from fractal import Pen

p = Pen([500, 500], title="Koch island")
p.setPoint([100, 100])
p.doD0L(omega="f-f-f-f", P={"f": "f+f-f-ff+f+f-f"},
        delta=90, times=4, length=300, rate=4)
p.wait()
