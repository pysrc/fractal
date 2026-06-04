"""
    迭代函数系统（IFS）
"""
from random import random
from math import sin, cos
from .base import Base, HAS_NUMPY


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
        Base.__init__(self, size, self._run, title)
        self.setPx()
        self.setIfsCode()
        self.__coo = True
        if color:
            self.color = color
        else:
            self.color = [255, 255, 255]
        self.fill(self.color)

    def setCoordinate(self):
        # 纵轴的反向
        self.__coo = not self.__coo

    def ifsp(self, x, y):
        # 变换规则(返回迭代后的坐标)
        return (x, y)

    def setIfsp(self, call):
        self.ifsp = call

    def setIfsCode(self, ifsCode=None):
        # 设置ifs码
        self.ifsCode = ifsCode
        if ifsCode != None:
            p = [i[-1] for i in self.ifsCode]
            self.__fn = len(p)
            sp = sum(p)
            self.__pe = [sum(p[:i + 1])/sp for i in range(self.__fn)]

    def __parseIfsCode(self, x, y):
        rand = random()
        i = 0
        while i < self.__fn:
            if rand <= self.__pe[i]:
                a, b, c, d, e, f, p = self.ifsCode[i]
                return (a * x + b * y + e, c * x + d * y + f)
            i += 1
        return (0, 0)

    def setPx(self, enlarge=1, pl=0, pt=0):
        # 平移、放大调整
        self.enlarge = enlarge
        self.pl = pl
        self.pt = pt

    def _run(self):
        start = self.start
        for i in range(self.n):
            px = int(self.enlarge * start[0] + self.pl)
            py = int(self.enlarge * start[1] + self.pt)
            if not self.__coo:
                py = self.height - py
            if HAS_NUMPY and self._pixel_array is not None:
                if 0 <= px < self.width and 0 <= py < self.height:
                    self._pixel_array[py, px] = [int(self.pcolor[0]), int(self.pcolor[1]), int(self.pcolor[2])]
            else:
                self.set_pixel_fast(px, py, self.pcolor[0], self.pcolor[1], self.pcolor[2])
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