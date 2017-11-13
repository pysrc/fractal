# Tree
from fractal import Pen

p = Pen([400,510])

p.setPoint([250,510])

p.setAngle(90)

p.doD0L(omega = "f", P = {"f": "ff+[+f-f-f]-[-f+f+f]"}, delta = 22.5, times = 4, length = 400, rate = 2.6)

p.save("tree2.jpg")

p.wait()