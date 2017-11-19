from fractal import Julia
ju = Julia([500, 500])
ju.setExp(4)
ju.setC(-0.5 + 0.49j)
ju.setRadius(5)
ju.doJulia(400)
ju.wait()
