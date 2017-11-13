from fractal import Pen

p = Pen([400, 450])

p.setAngle(90)

p.setPoint([200, 450])

p.doD0L(omega="f", P={"f": "h[-f]h[+f]-f", "h": "hh"},
        delta=22.5, times=7, length=400, rate=2.17)

p.wait()
