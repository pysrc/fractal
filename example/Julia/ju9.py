from fractal import Julia
ju = Julia([500, 500])
# ju.setC(0.3+0j)
ju.setC(-0.77 + 0.17j)
# ju.setC(0.43-0.2j)
# ju.setC(0.35+0.05j)
ju.doJulia(400)
ju.wait()
