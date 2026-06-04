"""
Julia集
"""

from .base import Base, HAS_NUMPY
from .colors import *
from threading import Thread


class Julia(Base):

    def __init__(self, size, title=""):
        Base.__init__(self, size, self._run, title)
        self.setExp(2)
        self.setC(None)
        self.setRadius(2)
        self.width = size[0]
        self.height = size[1]
        self.setRange(3.5, 3.5)
        self.setCentre(0 + 0j)

    def setRadius(self, R):
        # 设置逃逸半径
        self.R = R

    def setC(self, C):
        # 设置参考值C
        self.C = C

    def setExp(self, expc):
        # 设置指数，默认2
        self.expc = expc

    def color(self, n, r=2):
        if n < len(reds):
            return reds[n]
        else:
            if r < self.R:
                return blues[int((len(blues) - 1) * r / self.R)]
            else:
                return purples[int((len(purples) - 1) * self.R / r)]

    def setColor(self, call):
        self.color = call

    def setCentre(self, z0):
        # 设置中心点
        self.z0 = z0

    def setRange(self, xmax, ymax):
        # 设置坐标范围，范围越小图放大倍数越高
        self.xmax = xmax
        self.ymax = ymax

    def __getXY(self, i, j):
        # 通过像素坐标获取映射后的坐标
        return complex((i / self.width - 0.5) * self.xmax + self.z0.real,
                       (j / self.height - 0.5) * self.ymax + self.z0.imag)

    def scala(self, i, j, rate):
        # 将(i, j)像素点置于中心位置，放大rete倍
        self.setCentre(self.__getXY(i, j))
        self.xmax /= rate
        self.ymax /= rate

    def __calc(self, start, w, h):
        """计算子区域像素"""
        for i in range(start[0], start[0] + w):
            for j in range(start[1], start[1] + h):
                ct = 0
                z = self.__getXY(i, j)
                for k in range(self.N):
                    ct = k
                    if abs(z) > self.R:
                        break
                    z = z**self.expc + self.C
                col = self.color(ct, abs(z))
                # 直接写入numpy数组
                if HAS_NUMPY and self._pixel_array is not None:
                    self._pixel_array[j, i] = [int(col[0]), int(col[1]), int(col[2])]
                else:
                    self.set_pixel_fast(i, j, col[0], col[1], col[2])

    def _run(self):
        # 线程中
        print("x range ：[-%.2e,%.2e]\ny range ：[-%.2e,%.2e]" % (
            self.xmax, self.xmax, self.ymax, self.ymax))
        if self.C == None:
            raise Exception("请设置迭代常数")
        tn = 5  # 25 个子线程绘图
        ci = self.width // tn
        cj = self.height // tn
        ts = []
        for i in range(tn):
            for j in range(tn):
                t = Thread(target=self.__calc, args=([i * ci, j * cj], ci, cj))
                t.start()
                ts.append(t)
        for t in ts:
            t.join()
        del ts

    def doJulia(self, N):
        # 进入迭代
        # N: 单点最大迭代次数
        self.N = N