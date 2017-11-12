"""
L-系统生成法
"""

from math import sin, cos, pi
import pygame


def left(screen, st, angle, d):
    # st: 起点坐标
    # angle: 向左偏转的度数
    # d: 距离
    angle = pi * angle / 180
    return [st[0] + d * cos(angle), st[1] - d * sin(angle)]


class Pen:

    def __init__(self, size, title=""):
        # size 画布的宽高 [width, hight]
        # title 画布标题
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.screen.fill([255, 255, 255])
        self.setPoint([size[0] / 2, size[1] / 2])
        self.setColor([0, 0, 0])
        self.setWidth(2)
        self.setAngle(0)
        pygame.display.flip()

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
        pygame.display.flip()
        self.pos = np

    def doD0L(self, omega, P, delta, times, length, rate, delta0=0):
        # omega: 公理（初始字符串）
        # P: 产生式（映射规则）
        # delta0: 初始偏移量
        # delta: 角度增量
        # times: 迭代次数
        # length: 初始线长
        # rate: 每次迭代后缩小的倍数

        length /= (rate**times)
        for i in range(times):
            for key in P:
                omega = omega.replace(key, P[key])
        self.left(delta0)
        for j in omega:
            if j == '+':
                self.left(delta)
            elif j == '-':
                self.right(delta)
            else:
                self.forward(length)

    def edgeRewrite(self, omega, P, delta, times, length, rate, delta0=0):
        # 边改写
        length /= (rate**times)
        for i in range(times):
            ct = 0
            for key in P:
                omega = omega.replace(key, str(ct))
                ct += 1
            ct = 0
            for key in P:
                omega = omega.replace(str(ct), P[key])
                ct += 1
        self.left(delta0)
        for j in omega:
            if j == '+':
                self.left(delta)
            elif j == '-':
                self.right(delta)
            else:
                self.forward(length)

    def save(self, title):
        # 保存图片，title为文件名
        pygame.image.save(self.screen, title)

    def wait(self):
        # 绘制结束等用户关闭程序
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
