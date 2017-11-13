# FASS曲线
from fractal import Pen

p = Pen([420,420])

p.setPoint([10,10])

p.doD0L(omega = "L", P = {"L": "LFRFL-FF-RFLFR+FF+LFRFL", "R": "RFLFR+FF+LFRFL-FF-RFLFR"}, delta =  90, times = 4, length = 200 , rate = 3)

p.wait()