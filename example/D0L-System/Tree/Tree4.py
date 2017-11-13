from fractal import Pen

p = Pen([400, 470])

p.setAngle(90)

p.setPoint([200,470])

p.doD0L(omega = "f", P = {"f": "h[-f][+f]hf", "h": "hh"}, delta = 25.7, times = 7, length = 400, rate = 2.17)

p.wait()