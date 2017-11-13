# FASS曲线
from fractal import Pen

p = Pen([420,420])

p.setPoint([10,400])

p.doD0L(omega = "L", P = {"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "-LFLF+RFRFR+F+RF-LFL-FR"}, delta =  90, times = 4, length = 200 , rate = 3)

p.wait()