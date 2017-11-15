import pygame
from fractal.julia import colors


class Mandelbrot:

    def __init__(self, size, title=""):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.screen.fill([255, 255, 255])  # 白色填充
        self.setExp(2)
        self.setRadius(2)
        self.selectArea([0, 0], size[0], size[1])
        self.setZ0(0 + 0j)

    def setRadius(self, R):
        # 设置逃逸半径
        self.R = R

    def setZ0(self, Z0):
        # 设置起始迭代复数（一般为0+0j）
        self.Z0 = Z0

    def selectArea(self, start, width, height):
        # 产生 Mandelbrot 集的区域
        self.start = start
        self.width = int(width)
        self.height = int(height)

    def setExp(self, expc):
        # 设置指数，默认2
        self.expc = expc

    def color(self, i):
        # 对第i次迭代点着色，返回RGB值
        if i < 10:
            return [255, 255, 255]
        return colors[i % len(colors)]

    def setColor(self, call):
        self.color = call

    def doMandelbrot(self, N):
        # 开始迭代
        # N: 最大迭代次数
        for i in range(self.width):
            for j in range(self.height):
                ct = 0  # 当前迭代次数
                z = self.Z0
                c = complex(4 * i / self.width - 2,
                            4 * j / self.height - 2)
                for k in range(N):
                    ct = k
                    if abs(z) > self.R:  # 大于逃逸半径，则返回
                        break
                    z = z**2 + c
                self.screen.set_at(
                    [self.start[0] + i, self.start[1] + j], self.color(ct))
        pygame.display.flip()

    def save(self, title):
        # 保存图片，title为文件名
        pygame.image.save(self.screen, title)

    def wait(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
