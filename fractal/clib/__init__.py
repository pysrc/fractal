import ctypes

dll = ctypes.CDLL('fractal/clib/calc.dll')
juliaCalc = dll.juliaCalc
juliaCalc.argtypes = [ctypes.c_double * 13, ]
juliaCalc.restype = ctypes.c_int
k = (13 * ctypes.c_double)()

def calc(args):
    for i in range(13):
        k[i] = args[i]
    res = juliaCalc(k)
    return res, k[0]
