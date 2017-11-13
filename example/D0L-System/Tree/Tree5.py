from fractal import Pen

p = Pen([400, 470])

p.setAngle(90)

p.setPoint([170, 470])

p.doD0L(omega="f", P={"f": "h+[[f]-f]-h[-hf]+f", "h": "hh"},
        delta=22.5, times=6, length=400, rate=2.3)

p.wait()
