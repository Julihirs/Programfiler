import pygame

pygame.init()

storlek = [1280, 700]
skärm = pygame.display.set_mode(storlek)
bakgrund = pygame.image.load("space-7754181_1280.jpg").convert()
karaktär = pygame.image.load("Space invader ship.png").convert_alpha()
fiende = pygame.image.load('fiende.png').convert_alpha()
done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

fiendekoordinater = [[10,10]]

while fiendekoordinater[len(fiendekoordinater)-1][0] < 1000:
    fiendekoordinater.append([fiendekoordinater[len(fiendekoordinater)-1][0]+80,10])
fiendekoordinater.append([10,85])
while fiendekoordinater[len(fiendekoordinater)-1][0] < 1000:
    fiendekoordinater.append([fiendekoordinater[len(fiendekoordinater)-1][0]+80,85])
fiendekoordinater.append([10,160])
while fiendekoordinater[len(fiendekoordinater)-1][0] < 1000:
    fiendekoordinater.append([fiendekoordinater[len(fiendekoordinater)-1][0]+80,160])
fiendekoordinater.append([10,235])
while fiendekoordinater[len(fiendekoordinater)-1][0] < 1000:
    fiendekoordinater.append([fiendekoordinater[len(fiendekoordinater)-1][0]+80,235])
skottlista = []

x_speed = 0
y_speed = 0

x_kord = 640
y_kord = 600

högerkant = False
vänsterkant = False
right = True

level = 0
hej = 17
while not done:
    hej -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -5
            elif event.key == pygame.K_d:
                x_speed = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                x_speed = 0
        
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (hej <= 0):
            skottlista.append([x_kord,y_kord-55])
            hej = 17

    if (x_kord + x_speed + 40 < 1280) and (x_kord + x_speed - 40 > 0):
        x_kord = x_kord + x_speed
    

    skärm.blit(bakgrund,[0,0])

    räknare = 0
    for skot in skottlista:
        skottlista[räknare][1] -= 5
        pygame.draw.circle(skärm,[255,255,255],skot,2)
        räknare2 = 0
        for ENEMY in fiendekoordinater:
            if (ENEMY[0]+50 >= skot[0]) and (ENEMY[0] <= skot[0]) and (ENEMY[1]+50+level >= skot[1]) and (ENEMY[1]+level <= skot[1]):
                fiendekoordinater.__delitem__(räknare2)
                skottlista.__delitem__(räknare)
                räknare -= 1
            else:
                räknare2 += 1
        räknare += 1



    skärm.blit(karaktär,[x_kord - 40, 549])
    for ENEMY in fiendekoordinater:
        skärm.blit(fiende,[ENEMY[0], ENEMY[1]+level])
    räknare = 0
    lägstarad = 235
    hittatlägsta = False

    if right:
        extremX = 10
        for ENEMY in fiendekoordinater:
            fiendekoordinater[räknare][0] += 1 + level/60
            if ENEMY[0] > extremX:
                extremX = ENEMY[0]
            räknare += 1
            if not hittatlägsta:
                if ENEMY[1] == lägstarad:
                    hittatlägsta = True
            if extremX >= 1230:
                right = False
                level += 12
                break
        if not hittatlägsta:
            lägstarad -= 75
    else:
        for ENEMY in fiendekoordinater:
            fiendekoordinater[räknare][0] -= 1 + level/60
            if ENEMY[0] < extremX:
                extremX = ENEMY[0]
            räknare += 1
            if not hittatlägsta:
                if ENEMY[1] == lägstarad:
                    hittatlägsta = True
            if extremX <= 10:
                right = True
                level += 12
                break
        if not hittatlägsta:
            lägstarad -= 75
    if lägstarad+level+50 >= 560:
        done = True
        break
    pygame.display.flip()
    clock.tick(60)
pygame.quit()