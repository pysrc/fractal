# 龙曲线
from fractal import Pen
from math import sqrt
p = Pen([330, 250])
p.setPoint([240, 150])
p.edgeRewrite(omega="L", P={"L": "L+R", "R": "L-R"},
              delta=90, times=12, length=200, rate=sqrt(2))
p.wait()
