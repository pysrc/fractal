"""
    基类
    打印（保存图片）图片：Ctrl+P
    放大：点击放大部分鼠标左键
    缩小：点击缩小部分鼠标右键
"""

import pygame
from pygame.locals import K_p, K_LCTRL, K_RCTRL  # 按下Ctrl + P键打印
import threading
import time

class Base(object):

    def __init__(self, size, callRun, title=""):
        """
            size: 画布尺寸
            callRun: 子类的绘画函数回掉
            title: 画布标题
        """
        self.__run = callRun
        self.title = title
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.screen.fill([255, 255, 255])
        self.psave = False
        self.scalaRate = 4  # 放大（缩小）倍数
        self.ctrl = False  # Ctrl键按下
        self.cnt = 1  # 连续命名时标号

    def save(self, title):
        # 保存图片，title为文件名
        pygame.image.save(self.screen, title)

    def wait(self):
        # 等待用户关闭
        th = threading.Thread(target=self.__run)
        th.start()
        while 1:
            for event in pygame.event.get():
                if not th.is_alive():  # 必须绘图结束才可操作
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_p and self.ctrl:
                            if self.title == "":
                                self.title = "game"
                            self.save(self.title + str(self.cnt) + ".jpg")
                            self.ctrl = False
                            self.cnt += 1
                        if event.key == K_LCTRL or event.key == K_RCTRL:
                            self.ctrl = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 and hasattr(self, "scala"):  # 鼠标左键放大
                            i, j = event.pos
                            w = self.screen.get_width() // (2 * self.scalaRate)
                            h = self.screen.get_height() // (2 * self.scalaRate)
                            pygame.draw.rect(self.screen, [0, 0, 0], [
                                             i - w, j - h, 2 * w, 2 * h], 1)
                            pygame.display.flip()
                            self.scala(i, j, self.scalaRate)
                            th = threading.Thread(target=self.__run)
                            th.start()
                        # 鼠标右键缩小
                        elif event.button == 3 and hasattr(self, "scala"):
                            i, j = event.pos
                            self.scala(i, j, 1 / self.scalaRate)
                            th = threading.Thread(target=self.__run)
                            th.start()
            pygame.display.flip()
