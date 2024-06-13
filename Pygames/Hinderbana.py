import pygame
import time
import random

pygame.init()

DONE = False
klocka = pygame.time.Clock()
bredd, höjd = 800, 600
skärm = pygame.display.set_mode((bredd, höjd))

def kollision_hinder(spelare_x, spelare_y, hinder_x, hinder_y):
    if hinder_x <= spelare_x + 30 <= hinder_x + 30:
        if spelare_y >= hinder_y :
            return True
    if hinder_x <= spelare_x <= hinder_x + 30:
        if spelare_y >= hinder_y:
            return True
    return False

def ny_box():
    return random.randrange(400, 500)

# spelar koordinater
spelare_x = 385
spelare_y = 500
ändring_x = 0
ändring_y = 0
spelare_x_storlek = 30
spelare_y_storlek = 30

# hinder koordinater
hinder_x = 800
hinder_y = ny_box()

hinder_x2 = 1200
hinder_y2 = ny_box()

hopp = False
ducka = False

tid_kvar_som_ducka = 0.0

# spelloop
while not DONE:
    skärm.fill((159,222,249))
    # spelare
    pygame.draw.rect(skärm, (255,255,255), [spelare_x, spelare_y, spelare_x_storlek, spelare_y_storlek])
    pygame.draw.rect(skärm, (218, 191, 85), [0, 530, 800, 100])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        if not hopp:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hopp = True
                    ändring_y = -10
        if not ducka:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    ducka = True
                    spelare_y_storlek = 10
                    # starta nedräkning av tid börja på 2 sek
                    tid_kvar_som_ducka = 2.0

    if hopp == True:
        spelare_y = spelare_y + ändring_y
        ändring_y = ändring_y + 0.5
    if spelare_y >= 500:
        spelare_y = 500
        hopp = False
        ändring_y = 0

    if ducka and tid_kvar_som_ducka > 0: # och om tiden > 0
        # när vi precis duckar
        spelare_y = 520
    if ducka and tid_kvar_som_ducka < 0:
        # när tiden för duckning går ut => återställa bara en gång

        spelare_y = 500
        spelare_y_storlek = 30
        ducka = False
    
    spelare_y += ändring_y

    # hinder 1
    pygame.draw.rect(skärm, (0,0,0), [hinder_x, hinder_y, 30, 30])
    hinder_x -= 5
    if hinder_x <= -30:
        hinder_x = 800
        hinder_y = ny_box()
    
    #hinder 2
    pygame.draw.rect(skärm, (0,0,0), [hinder_x2, hinder_y2, 30, 30])
    hinder_x2 -= 5
    if hinder_x2 <= -30:
        hinder_x2 = 800
        hinder_y2 = ny_box()
    
    # kollision med hinder
    if kollision_hinder(spelare_x, spelare_y, hinder_x, hinder_y):
        DONE = True
    if kollision_hinder(spelare_x, spelare_y, hinder_x2, hinder_y2):
        DONE = True

    pygame.display.update()
    tid_kvar_som_ducka -= 1.0/60
    klocka.tick(60)
pygame.quit()
quit()