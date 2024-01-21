import pygame

pygame.init()
win = pygame.display.set_mode((600, 400))

x = 100
y = 50
x1 = 100
y1 = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))

    x = x + 1
    y1 = y1 + 1
    if x > 600:
        x = 0

    if y1 > 400:
        y1 = 0

    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))

    pygame.draw.circle(win, (255, 0, 0), (x1, y1), 30)
    pygame.display.update()
    pygame.time.delay(10)
