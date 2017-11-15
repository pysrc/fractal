"""
    基类
"""

import pygame
import threading


class Base(object):

    def __init__(self, size,callRun, title=""):
        """
            size: 画布尺寸
            callRun: 子类的绘画函数回掉
            title: 画布标题
        """
        self.__run = callRun
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.screen.fill([255, 255, 255])
        self.psave = False

    def save(self, title):
        # 保存图片，title为文件名
        self.psave = True
        self.ftitle = title

    def wait(self):
        # 等待用户关闭
        th = threading.Thread(target=self.__run)
        th.start()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if not th.is_alive():
                if self.psave:
                    pygame.image.save(self.screen, self.ftitle)
            pygame.display.flip()
