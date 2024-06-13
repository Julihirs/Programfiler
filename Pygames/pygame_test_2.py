import pygame
x = 1200
y = 700
SCREEN = pygame.display.set_mode([x,y])
CLOCK = pygame.time.Clock()
pygame.display.init()
RUN = True
JUMP = False
WHELD = False
X_SPEED = 1200/(60*2)
Y_SPEED = 20
PLAYER = 430
HILLS_CORD = [1200, 430]
HILLS_SIZE = [50, 70]
SUN = 400
cloud1 = 200
cloud2 = 200
cloud3 = 250
cloud4 = 300

cloud5 = 600
cloud6 = 700
cloud7 = 650
cloud8 = 600

cloud9 = 1000
cloud10 = 1000
cloud11 = 1050
cloud12 = 1100

cloud13 = 900
cloud14 = 900
cloud15 = 915
cloud16 = 930

cloud17=100
cloud18=96
cloud19=120
cloud20=147

while RUN:
    for action in pygame.event.get():
        print(action.type, action)
        KEYBOARD = pygame.key.get_pressed()
        if not JUMP:
            if action.type == 768:
                JUMP = True
        if action.type == pygame.QUIT:
            pygame.quit()
    if JUMP:
        PLAYER = PLAYER - Y_SPEED
        Y_SPEED = Y_SPEED - 1
        if PLAYER == 430:
            JUMP = False
            Y_SPEED = 20

    HILLS_CORD[0] = HILLS_CORD[0] - X_SPEED
    if HILLS_CORD[0] <= - HILLS_SIZE[0]/2:
        HILLS_CORD[0] = 1200 + HILLS_SIZE[0]/2
    
    if PLAYER == 430 and HILLS_CORD[0] == 360:
        pygame.quit()

    SUN = SUN + (1/29)

    cloud1 = cloud1 - (1/5)
    cloud2 = cloud2 - (1/5)
    cloud3 = cloud3 - (1/5)
    cloud4 = cloud4 - (1/5)

    cloud5 = cloud5 - (1/5)
    cloud6 = cloud6 - (1/5)
    cloud7 = cloud7 - (1/5)
    cloud8 = cloud8 - (1/5)

    cloud9 = cloud9 - (1/5)
    cloud10 = cloud10 - (1/5)
    cloud11 = cloud11 - (1/5)
    cloud12 = cloud12 - (1/5)

    cloud13 = cloud13 - (1/5)
    cloud14 = cloud14 - (1/5)
    cloud15 = cloud15 - (1/5)
    cloud16 = cloud16 - (1/5)

    cloud17 = cloud17 - (1/5)
    cloud18 = cloud18 - (1/5)
    cloud19 = cloud19 - (1/5)
    cloud20 = cloud20 - (1/5)

    # sky
    pygame.draw.rect(SCREEN, [255, 112, 169], pygame.Rect(0,0, 1200,500))
    pygame.draw.rect(SCREEN, [255, 94, 158], pygame.Rect(0,0, 1200,480))
    pygame.draw.rect(SCREEN, [255, 79, 149], pygame.Rect(0,0, 1200,460))
    pygame.draw.rect(SCREEN, [255, 66, 141], pygame.Rect(0,0, 1200,440))
    pygame.draw.rect(SCREEN, [255, 54, 133], pygame.Rect(0,0, 1200,420))
    pygame.draw.rect(SCREEN, [255, 38, 123], pygame.Rect(0,0, 1200,400))
    pygame.draw.rect(SCREEN, [255, 23, 114], pygame.Rect(0,0, 1200,380))
    pygame.draw.rect(SCREEN, [255, 13, 108], pygame.Rect(0,0, 1200,360))
    pygame.draw.rect(SCREEN, [255, 3, 102], pygame.Rect(0,0, 1200,340))
    # sun
    pygame.draw.circle(SCREEN, [255, 247, 133], [600,SUN], 90)
    # ground
    pygame.draw.rect(SCREEN, [230, 198, 124], pygame.Rect(0,500, 1200,700))
    pygame.draw.rect(SCREEN, [237, 207, 135], pygame.Rect(0,500, 1200,55))
    # clouds
    pygame.draw.rect(SCREEN, [252, 189, 214], pygame.Rect(cloud1,200, 100,50))
    pygame.draw.circle(SCREEN, [252, 189, 214], [cloud2,215], 35)
    pygame.draw.circle(SCREEN, [252, 197, 219], [cloud3,195], 40)
    pygame.draw.circle(SCREEN, [252, 189, 214], [cloud4,215], 35)

    pygame.draw.rect(SCREEN, [252, 189, 214], pygame.Rect(cloud5,115, 100,50))
    pygame.draw.circle(SCREEN, [252, 189, 214], [cloud6,130], 35)
    pygame.draw.circle(SCREEN, [252, 197, 219], [cloud7,100], 40)
    pygame.draw.circle(SCREEN, [252, 189, 214], [cloud8,130], 35)
    
    pygame.draw.rect(SCREEN, [252, 189, 214], pygame.Rect(cloud9,300, 100,50))
    pygame.draw.circle(SCREEN, [252, 189, 214], [cloud10,315], 35)
    pygame.draw.circle(SCREEN, [252, 197, 219], [cloud11,300], 40)
    pygame.draw.circle(SCREEN, [252, 189, 214], [cloud12,315], 35)

    pygame.draw.rect(SCREEN, [247, 148, 188], pygame.Rect(cloud13,200, 30,15))
    pygame.draw.circle(SCREEN, [247, 148, 188], [cloud14,205], 10)
    pygame.draw.circle(SCREEN, [247, 148, 188], [cloud15,200], 15)
    pygame.draw.circle(SCREEN, [247, 148, 188], [cloud16,205], 10)

    pygame.draw.rect(SCREEN, [247, 148, 188], pygame.Rect(cloud17,100, 50,25))
    pygame.draw.circle(SCREEN, [247, 148, 188], [cloud18,105], 20)
    pygame.draw.circle(SCREEN, [247, 148, 188], [cloud19,97], 25)
    pygame.draw.circle(SCREEN, [247, 148, 188], [cloud20,105], 20)
    # player
    pygame.draw.rect(SCREEN, [71, 196, 16], pygame.Rect(300,PLAYER, 70,70))
    # hills
    pygame.draw.rect(SCREEN, [237, 207, 135], pygame.Rect(HILLS_CORD, HILLS_SIZE))

    pygame.display.flip()
    CLOCK.tick(60)
pygame.quit()