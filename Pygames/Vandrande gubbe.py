import pygame

# färger
svart = (0, 0, 0)
vit = (255, 255, 255)
grön = (0, 255, 0)
röd = (255, 0, 0)
 
def stick_figur(skärm, x, y):
    # huvud
    pygame.draw.ellipse(skärm, röd, [1 + x, y, 10, 10], 0)
    # ben
    pygame.draw.line(skärm, svart, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(skärm, svart, [5 + x, 17 + y], [x, 27 + y], 2)
    # kropp
    pygame.draw.line(skärm, grön, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    # armar
    pygame.draw.line(skärm, grön, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(skärm, grön, [5 + x, 7 + y], [1 + x, 17 + y], 2)
 
pygame.init()

storlek = [800, 600]
skärm = pygame.display.set_mode(storlek)

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)


x_speed = 0
y_speed = 0

x_kord = 400
y_kord = 300

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -3
            elif event.key == pygame.K_d and x_kord < 700:
                x_speed = 3  
            elif event.key == pygame.K_w:
                y_speed = -3
            elif event.key == pygame.K_s:
                y_speed = 3
            else :
                x_speed = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed = 0
        
        elif x_kord > 800:
            x_kord = 800
        elif x_kord < 0:
            x_kord = 800
        elif y_kord < 0:
            y_kord = 600
        elif y_kord > 600:
            y_kord = 0
    
    x_kord = x_kord + x_speed
    y_kord = y_kord + y_speed

    skärm.fill(vit)

    stick_figur(skärm, x_kord, y_kord)

    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()