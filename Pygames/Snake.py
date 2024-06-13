import pygame
import time
import random

pygame.init()
SKÄRM = pygame.display.set_mode((800,600))
DONE = False

CLOCK = pygame.time.Clock()

def SNAKE(SNAKE_LIST):
    for x in SNAKE_LIST:
        pygame.draw.rect(SKÄRM, (0,255,0), [x[0], x[1], 30, 30])
        pygame.draw.lines(SKÄRM,[0,0,0],True,[x,[x[0]+30,x[1]],[x[0]+30,x[1]+30],[x[0],x[1]+30]])

X = 400
Y = 300
X_change = 0
Y_change = 0

SNAKE_LIST = []
SNAKE_LÄNGD = 1

MAT_X = (random.randrange(0, 800))
MAT_Y = (random.randrange(0, 600))

while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                X_change = -6
                Y_change = 0
            elif event.key == pygame.K_d:
                X_change = 6
                Y_change = 0
            elif event.key == pygame.K_w:
                Y_change = -6
                X_change = 0
            elif event.key == pygame.K_s:
                Y_change = 6
                X_change = 0
    if X >= 770 or X < 0 or Y >= 570 or Y < 0:
        DONE = True
   
    X += X_change
    Y += Y_change
    SKÄRM.fill((185,153,174))
    pygame.draw.rect(SKÄRM, (0,255,0), [X,Y,30,30])
    pygame.draw.rect(SKÄRM, (255,0,0), [MAT_X, MAT_Y, 30, 30])
    SNAKE_HUVUD = []
    SNAKE_HUVUD.append(X)
    SNAKE_HUVUD.append(Y)
    SNAKE_LIST.append(SNAKE_HUVUD)
    if len(SNAKE_LIST) > SNAKE_LÄNGD:
        del SNAKE_LIST[0]
    for x in SNAKE_LIST[:-1]:
        if x == SNAKE_HUVUD:
            DONE = True
    
    # Kollisionsdetektion mellan ormens huvud och maten
    if ((MAT_X <= (X) <= (MAT_X + 30)) or (MAT_X <= (X+30) <= (MAT_X + 30))) and ((MAT_Y < Y < (MAT_Y + 30)) or (MAT_Y <= (Y+30) <= (MAT_Y + 30))):
        MAT_X = random.randrange(0, 800)
        MAT_Y = random.randrange(0, 600)
        SNAKE_LÄNGD += 5

    SNAKE(SNAKE_LIST)
    pygame.display.update()
    
    CLOCK.tick(60)

pygame.quit()
quit()

