# 皮亚洛曲线
from fractal import Pen
p = Pen([500, 500])
p.setPoint([85, 85])
p.setWidth(1)
p.doD0L(omega="R", P={"L": "L-R--R+L++LL+R-",
                            "R": "+L-RR--R-L++L+R"}, delta=60, times=4, length=139, rate=2)
p.wait()
