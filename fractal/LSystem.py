"""
    L-System for fractal
    已完成功能：
        1.简单D0L-系统
        2.合成D0L-系统
        3.简单分叉结构
    待完成功能：
        1.带年龄树（分叉）的生成
        2.随机L-系统
        3.参数L-系统
"""

from math import sin, cos, pi
import pygame
from .base import Base


def left(screen, st, angle, d):
    # st: 起点坐标
    # angle: 向左偏转的度数
    # d: 距离
    angle = pi * angle / 180
    return [st[0] + d * cos(angle), st[1] - d * sin(angle)]


class Pen(Base):

    def __init__(self, size, title=""):
        # size 画布的宽高 [width, hight]
        # title 画布标题
        Base.__init__(self, size, self.__run, title)
        self.setPoint([size[0] / 2, size[1] / 2])
        self.setColor([0, 0, 0])
        self.setWidth(1)
        self.setAngle(0)

    def setAngle(self, angle):
        self.angle = angle

    def setPoint(self, pos):
        # 设置笔的位置
        self.pos = pos

    def setWidth(self, width):
        # 设置线宽
        self.width = width

    def setColor(self, color):
        # 设置颜色
        self.color = color

    def left(self, angle):
        # 向左转angle度
        self.angle = self.angle + angle

    def right(self, angle):
        # 向右转angle度
        self.angle = self.angle - angle

    def forward(self, d):
        # 向前走d步长
        np = left(self.screen, self.pos, self.angle, d)
        pygame.draw.line(self.screen, self.color, self.pos, np, self.width)
        self.pos = np

    def __run(self):
        # 线程
        self.draw(self.omega, self.P, self.delta, self.length)

    def draw(self, omega, P, delta, length):
        i = 0
        while i < len(omega):
            if omega[i] == '+':
                self.left(delta)
            elif omega[i] == '-':
                self.right(delta)
            elif omega[i] == '[':
                k = 0
                st = i
                while i < len(omega):
                    if omega[i] == "[":
                        k += 1
                    elif omega[i] == "]":
                        k -= 1
                    if k == 0:
                        break
                    i += 1
                sub = omega[st + 1:i]
                curpoint = self.pos[:]
                curangle = self.angle
                self.draw(sub, P, delta, length)
                self.pos = curpoint
                self.angle = curangle
            else:
                self.forward(length)
            i += 1

    def doD0L(self, omega, P, delta, times, length, rate):
        # omega: 公理（初始字符串）
        # P: 产生式（映射规则）
        # delta: 角度增量
        # times: 迭代次数
        # length: 初始线长
        # rate: 每次迭代后缩小的倍数
        length /= (rate**times)
        for i in range(times):  # 完成字符串迭代
            ct = 0
            for key in P:
                omega = omega.replace(key, str(ct))
                ct += 1
            ct = 0
            for key in P:
                omega = omega.replace(str(ct), P[key])
                ct += 1
        self.omega = omega
        self.P = P
        self.delta = delta
        self.length = length
