import pygame
import random

#färger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 225, 0)
RED = (255, 0, 0)

pygame.init()

#lite variabler som ska in i the main loop
size = (700, 500)
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
done = False
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5

snow_list = []
for i in range(50):
        x = random.randrange(0, 700)
        y = random.randrange(0, 500)
        snow_list.append ([x, y])

# main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [rect_x,rect_y,50,50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    for item in snow_list:
        item[1] += 1
        pygame.draw.circle(screen, WHITE, item, 2)
        if item[1] > 500:
            item[1] = random.randrange(-20, -5)
            item[0] = random.randrange(700)
        if item > 500:
             item = item * -1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()