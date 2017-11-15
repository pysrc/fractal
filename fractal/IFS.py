"""
    迭代函数系统（IFS）
"""
import pygame
from random import random
from math import sin, cos
from .base import Base


def getIfsCode(matrix):
    # 极坐标形式变换到矩阵
    res = []
    for i in matrix:
        r, s, the, fu, e, f, p = i
        item = [r * cos(the), -s * sin(fu), r * sin(the), s * cos(fu), e, f, p]
        res.append(item)
    return res


class IFS(Base):

    def __init__(self, size, title="", color=None):
        Base.__init__(self, size, self.__run, title)
        self.setPx()
        self.setIfsCode()
        self.__coo = True
        if color:
            self.color = color
        else:
            self.color = [255, 255, 255]
        self.screen.fill(self.color)

    def setCoordinate(self):
        # 纵轴的反向
        self.__coo = not self.__coo

    def ifsp(self, x, y):
        # 变换规则(返回迭代后的坐标)
        # 此函数具体用时需要重写
        return (x, y)

    def setIfsp(self, call):
        self.ifsp = call

    def setIfsCode(self, ifsCode=None):
        # 设置ifs码
        self.ifsCode = ifsCode

    def __parseIfsCode(self, x, y):
        # 解析ifs码
        p = [i[-1] for i in self.ifsCode]  # 每个方程的概率
        fn = len(p)  # 方程个数
        sp = sum(p)
        pe = [sum(p[:i + 1]) for i in range(fn)]  # 将概率映射到0-1区间
        rand = random()
        i = 1
        while i < fn:
            if rand < pe[i]:
                break
            i += 1
        i -= 1
        # 选择概率pe[i]对应的方程
        a, b, c, d, e, f, p = self.ifsCode[i]
        return (a * x + b * y + e, c * x + d * y + f)

    def setPx(self, enlarge=1, pl=0, pt=0):
        # 平移、放大调整
        # enlarge: 放大倍数
        # pl: 向右平移像素
        # pt: 向下平移像素
        self.enlarge = enlarge
        self.pl = pl
        self.pt = pt

    def __run(self):
        start = self.start
        for i in range(self.n):
            if self.__coo:
                self.screen.set_at(
                    (int(self.enlarge * start[0] + self.pl), int(self.enlarge * start[1] + self.pt)), self.pcolor)
            else:
                self.screen.set_at((int(self.enlarge * start[0] + self.pl), self.screen.get_height(
                ) - int(self.enlarge * start[1] + self.pt)), self.pcolor)
            start = self.ifsp(*start)

    def doIFS(self, n, start=None, color=None):
        """
            开始迭代
            start: 迭代起点
            color: 描点的颜色
        """
        self.n = n
        if start == None:
            self.start = (0, 0)
        else:
            self.start = start
        if color == None:
            self.pcolor = [0, 0, 0]
        else:
            self.pcolor = color
        if self.ifsCode != None:
            self.ifsp = self.__parseIfsCode
