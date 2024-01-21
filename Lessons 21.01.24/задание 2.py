import pygame

pygame.init()
win = pygame.display.set_mode((600, 400))

x = 100
y = 50
x1 = 100
y1 = 50

direction = 1
directionY = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))


    x = x + direction
    y1 = y1 + directionY
    if x > 600:
        direction = -1
    if x < 0:
        direction = 1
    if y1 > 400:
        directionY = -1
    if y1 < 0:
        directionY = 1


    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))

    pygame.draw.circle(win, (255, 0, 0), (x1, y1), 30)
    pygame.display.update()
    pygame.time.delay(10)
