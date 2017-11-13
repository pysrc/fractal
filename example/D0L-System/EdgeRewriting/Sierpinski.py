from fractal import Pen

p = Pen([500,500])

p.setPoint([10, 490])

p.doD0L(omega = "R", P = {"L":"R+L+R", "R": "L-R-L"}, delta = 60, times = 8, length = 450, rate = 2)

p.wait()