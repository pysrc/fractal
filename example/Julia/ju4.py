from fractal import Julia
ju = Julia([500, 500])
ju.setC(0.2 + 0.65j)
ju.doJulia(500)
ju.wait()
