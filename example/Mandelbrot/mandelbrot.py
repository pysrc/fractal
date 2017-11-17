from fractal import Mandelbrot
man = Mandelbrot([500, 500])
man.setRange(5, 5)
man.doMandelbrot(200)
man.wait()