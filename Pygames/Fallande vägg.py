import pygame
from pygame.locals import *
import time
import random

level = 0
i = 0

lista_färger = [(245,50,50),(245,50,173),(225,50,245),(128,50,245),(57,50,245),(50,173,245),(50,238,245),(50,245,160),(50,245,63),(245,238,50),(245,160,50)]

def få_nytt_hål():
    return random.randrange(50, 750)

def kollision(spelare_x, spelare_y, vägg_y, mitten_hål):
    if vägg_y <= spelare_y <= vägg_y + 40:
        if spelare_x <= mitten_hål - 50 or spelare_x >= mitten_hål + 20:
            return True
    if vägg_y <= spelare_y + 30 <= vägg_y + 40:
        if spelare_x <= mitten_hål - 50 or spelare_x >= mitten_hål + 20:
            return True
    return False

def uppdatera_text(i):
    return font.render(f'Passerade väggar: {i}', True, (255,255,255))

def vägg_ny_färg():
    return random.choice(lista_färger)

pygame.init()
pygame.font.init()
pygame.mixer.init()

ljud = pygame.mixer.Sound('din-ding-89718.mp3')
DONE = False
klocka = pygame.time.Clock()
bredd, höjd = 800, 600
skärm = pygame.display.set_mode((bredd, höjd))

# text
font = pygame.font.SysFont('Verdana', 30)
text = uppdatera_text(i)

# spelar koordinater
spelare_x = 385
spelare_y = 285
ändring_x = 0
ändring_y = 0

# Väggkoordinater
vägg_y = -50
vägg_2y = -400

# hålkoordinater
mitten_hål = få_nytt_hål()
mitten_hål2 = få_nytt_hål()

# passera väggar
passera_vägg_1 = False
passera_vägg_2 = False

random_färg = vägg_ny_färg()
random_färg2 = vägg_ny_färg()

# spelloop
while not DONE:
    skärm.fill((0,0,0))
    # spelare
    pygame.draw.rect(skärm, (255,255,255), [spelare_x, spelare_y, 30, 30])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        if event.type == pygame.KEYDOWN:
            if event.key in {pygame.K_a, pygame.K_LEFT}:
                ändring_x = -7.4
            elif event.key in {pygame.K_d, pygame.K_RIGHT}:
                ändring_x = 7.4
            if event.key in {pygame.K_w, pygame.K_UP}:
                ändring_y = -7.4
            elif event.key in {pygame.K_s, pygame.K_DOWN}:
                ändring_y = 7.4
        if event.type == pygame.KEYUP:
            if event.key in {pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_RIGHT}:
                ändring_x = 0
            if event.key in {pygame.K_w, pygame.K_UP, pygame.K_s, pygame.K_DOWN}:
                ändring_y = 0
    if spelare_x >= 770:
        spelare_x = 770
    if spelare_x <= 0:
        spelare_x = 0
    if spelare_y >= 570:
        spelare_y = 570
    if spelare_y <= 0:
        spelare_y = 0
    
    spelare_x += ändring_x
    spelare_y += ändring_y

    # vägg 1
    pygame.draw.rect(skärm, (random_färg), [0, vägg_y, mitten_hål - 50, 40]) 
    pygame.draw.rect(skärm, (random_färg), [mitten_hål + 50, vägg_y, 800 - (mitten_hål + 50), 40])
    vägg_y += 7 - (4/(level+1))
    if vägg_y >= 650:
        vägg_y = -50
        mitten_hål = få_nytt_hål()
        level += 0.1
        passera_vägg_1 = False
        random_färg = vägg_ny_färg()

    # vägg 2
    pygame.draw.rect(skärm, (random_färg2), [0, vägg_2y, mitten_hål2 - 50, 40])
    pygame.draw.rect(skärm, (random_färg2), [mitten_hål2 + 50, vägg_2y, 800 - (mitten_hål2 + 50), 40])
    vägg_2y += 7 - (4/(level+1))
    if vägg_2y >= 650:
        vägg_2y = -50
        mitten_hål2 = få_nytt_hål()
        passera_vägg_2 = False
        random_färg2 = vägg_ny_färg()
        
    # Kollision med vägg
    if kollision(spelare_x, spelare_y, vägg_y, mitten_hål):
        DONE = True
    if kollision(spelare_x, spelare_y, vägg_2y, mitten_hål2):
        DONE = True

    # Kontrollera om spelaren passerar genom hål i vägg 1
    if not passera_vägg_1 and vägg_y < spelare_y < vägg_y + 40:
        if mitten_hål - 50 < spelare_x < mitten_hål + 20:
            i += 1
            text = uppdatera_text(i)
            passera_vägg_1 = True
            ljud.play()

    # Kontrollera om spelaren passerar genom hål i vägg 2
    if not passera_vägg_2 and vägg_2y < spelare_y < vägg_2y + 40:
        if mitten_hål2 - 50 < spelare_x < mitten_hål2 + 20:
            i += 1
            text = uppdatera_text(i)
            passera_vägg_2 = True
            ljud.play()

    # text på skärm
    skärm.blit(text, (260, 20))

    pygame.display.update()
    klocka.tick(60)
pygame.quit()
quit()