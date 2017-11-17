from fractal import Julia
ju = Julia([500,500])
ju.setC(-0.605-0.45j)
ju.doJulia(200)
ju.wait()