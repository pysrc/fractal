from fractal import Julia
ju = Julia([500, 500])
ju.setC(-1.25 + 0j)
ju.doJulia(500)
ju.wait()
