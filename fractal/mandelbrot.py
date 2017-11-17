import pygame
from .colors import *
from .base import Base


class Mandelbrot(Base):

    def __init__(self, size, title=""):
        Base.__init__(self, size, self.__run, title)
        self.setExp(2)
        self.setRadius(2)
        self.setZ0(0 + 0j)
        self.width = size[0]
        self.height = size[1]
        self.setRange(3.5, 3.5)
        self.setCentre(0 + 0j)

    def setRadius(self, R):
        # 设置逃逸半径
        self.R = R

    def setZ0(self, Z0):
        # 设置起始迭代复数（一般为0+0j）
        self.Z0 = Z0

    def setCentre(self, z0):
        # 设置中心点
        self.z0 = z0

    def setRange(self, xmax, ymax):
        # 设置坐标范围，范围越小图放大倍数越高
        self.xmax = xmax
        self.ymax = ymax

    def __getXY(self, i, j):
        # 通过像素坐标获取映射后的坐标
        return complex((i / self.width - 0.5) * self.xmax + self.z0.real, (j / self.height - 0.5) * self.ymax + self.z0.imag)

    def scala(self, i, j, rate):
        # 将(i, j)像素点置于中心位置，放大rete倍
        self.setCentre(self.__getXY(i, j))
        self.xmax /= rate
        self.ymax /= rate

    def setExp(self, expc):
        # 设置指数，默认2
        self.expc = expc

    def color(self, i, r=2):
        # 对第i次迭代点着色，返回RGB值
        if i < len(reds) - 1:
            return reds[i]
        return (0, 0, 0)

    def setColor(self, call):
        self.color = call

    def __run(self):
        # 绘图
        N = self.N
        for i in range(self.width):
            for j in range(self.height):
                ct = 0  # 当前迭代次数
                z = self.Z0
                c = self.__getXY(i, j)
                for k in range(N):
                    ct = k
                    if abs(z) > self.R:  # 大于逃逸半径，则返回
                        break
                    z = z**self.expc + c
                self.screen.set_at([i, j], self.color(ct))

    def doMandelbrot(self, N):
        # 开始迭代
        # N: 最大迭代次数
        self.N = N
