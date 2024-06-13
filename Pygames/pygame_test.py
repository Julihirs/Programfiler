import pygame
bredd = 1200
höjd = 700
skärm = pygame.display.set_mode([bredd,höjd])
klocka = pygame.time.Clock()
pygame.display.init()
run = True
jump = False
wheld = False
playery = 350
hinderkoordinater = [800,350]
hinderstorlek = [85,75]
yfart = 20
xfart = 1200/(60 * 20)
while run:
    # gräs
    skärm.fill([98,189,115])
    # himmel
    pygame.draw.rect(skärm,[137,199,217],pygame.Rect(0,0,1200,383))
    # spelare
    pygame.draw.rect(skärm,[255,80,100],pygame.Rect(600-66/2,playery-66/2,66,66))
    # hinder
    pygame.draw.rect(skärm,[98,189,115], pygame.Rect(hinderkoordinater[0]-hinderstorlek[0]/2,hinderkoordinater[1]-hinderstorlek[1]/2,hinderstorlek[0],hinderstorlek[1]))
    # mittpunkter
    pygame.draw.circle(skärm,[255,255,255],hinderkoordinater,5)
    pygame.draw.circle(skärm,[255,255,255],[600,playery],5)
    for action in pygame.event.get():
        print(action.type, action)
        tangentbord = pygame.key.get_pressed()
        if not jump:
            if action.type == 768:
                jump = True
        if action.type == pygame.QUIT:
            pygame.quit()
    if wheld:
        skärm.fill([255,255,255,0.5])
    if jump:
        playery = playery - yfart
        yfart = yfart-1
        if playery == 350:
            jump = False
            yfart = 20
    hinderkoordinater[0] = hinderkoordinater[0] - xfart
    if hinderkoordinater[0] <= -hinderstorlek[0]/2:
        hinderkoordinater[0] = 1200+hinderstorlek[0]/2
    pygame.display.flip() 
    klocka.tick(60)
pygame.quit()