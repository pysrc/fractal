from fractal import Julia
from fractal.colors import *

def color(i, r=2):
    if i < len(reds) - 1:
        return reds[i]
    return (0, 0, 0)

k = -0.649 - 0.481j
ep = 5
ju = Julia([500, 500], title = "%s_%s"%(ep,k))
ju.setExp(ep)
ju.setC(k)
ju.setColor(color)
ju.doJulia(200)
ju.wait()
