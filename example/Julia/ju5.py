from fractal import Julia
ju = Julia([500, 500])
ju.setC(-0.7 + 0.38j)
ju.doJulia(500)
ju.wait()
