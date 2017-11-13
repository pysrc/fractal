"""
    IFS
"""
import pygame


class IFS:

    def __init__(self, size, title="", color=None):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.enlarge = 1
        self.pl = 0
        self.pt = 0
        if color:
            self.color = color
        else:
            self.color = [255, 255, 255]
        self.screen.fill(self.color)

    def ifsp(self, x, y):
        # 变换规则(返回迭代后的坐标)
        return (x, y)

    def setPx(self, enlarge, pl, pt):
        # 平移、放大调整
        # enlarge: 放大倍数
        # pl: 向右平移像素
        # pt: 向下平移像素
        self.enlarge = enlarge
        self.pl = pl
        self.pt = pt

    def doIFS(self, n, start=None, color=None):
        # 迭代
        if start == None:
            start = (0, 0)
        if color == None:
            color = [0, 0, 0]
        for i in range(n):
            self.screen.set_at(
                (int(self.enlarge * start[0] + self.pl), int(self.enlarge * start[1] + self.pt)), color)
            start = self.ifsp(*start)
        pygame.display.flip()

    def save(self, title):
        # 保存图片，title为文件名
        pygame.image.save(self.screen, title)

    def wait(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
