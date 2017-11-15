from fractal import Julia
ju = Julia([500, 500])
ju.setC(-1 + 0.05j)
ju.doJulia(500)
ju.wait()
