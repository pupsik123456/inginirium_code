import pygame


pygame.init()

width = 500
height = 500


win = pygame.display.set_mode((width, height))

xCircle = width / 2
yCircle = height / 2

color = (255, 0, 0)

cx = width / 2
cy = height / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xCircle -= 1
    elif keys[pygame.K_RIGHT]:
        xCircle += 1
    elif keys[pygame.K_UP]:
        yCircle -= 1
    elif keys[pygame.K_DOWN]:
        yCircle += 1
    else:
        xCircle = width / 2
        yCircle = height / 2

    if xCircle > cx + 150:
        color = (255, 255, 0)
    if xCircle < cx - 150:
        color = (139, 0, 0)
    if yCircle > cy + 250:
        color = (139, 0, 0)
    if yCircle < cy - 250:
        color = (255, 255, 0)




    win.fill((255, 255, 255))
    pygame.draw.circle(win, color, (xCircle, yCircle), 30)
    pygame.display.update()
    pygame.time.delay(10)



