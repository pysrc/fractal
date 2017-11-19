# C 库封装

import sys
import os
import ctypes

# 当前文件所处的文件夹
__curdir = os.path.split(os.path.realpath(__file__))[0]
__dll = None

if sys.platform == "win32":  # Windows
    if "32 bit" in sys.version:
        __dll = ctypes.CDLL(os.path.join(__curdir, "calc.dll"))
    else:  # 64位
        __dll = ctypes.CDLL(os.path.join(__curdir, "calc64.dll"))

__jCalc = __dll.jCalc
__jCalc.argtypes = [ctypes.c_double * 13, ]
__jCalc.restype = ctypes.c_int
__mCalc = __dll.mCalc
__mCalc.argtypes = [ctypes.c_double * 13, ]
__mCalc.restype = ctypes.c_int


def jCalc(args):
    k = (13 * ctypes.c_double)()
    for i in range(13):
        k[i] = args[i]
    res = __jCalc(k)
    r = k[0]
    del k
    return res, r


def mCalc(args):
    k = (13 * ctypes.c_double)()
    for i in range(13):
        k[i] = args[i]
    res = __mCalc(k)
    r = k[0]
    del k
    return res, r
