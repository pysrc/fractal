import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([500, 500])
img = pygame.image.load("reds.jpg").convert_alpha()
screen.blit(img, [0, 0])
pygame.display.flip()
res = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 取色保存
            if event.button == 1:  # 左键取色
                cl = screen.get_at(event.pos)
                y = event.pos[1]  # 获取高
                for i in range(500):
                    cl = screen.get_at([i, y])
                    if cl != (0, 0, 0):
                        res.append(cl[:3])
                    else:
                        print("end")
                        break
            elif event.button == 3:  # 右键保存
                with open("res.txt", "a") as f:
                    f.write(str(res) + "\n")
                res.clear()
