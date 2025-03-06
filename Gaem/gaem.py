import pygame
from sys import exit
import random

pygame.init()
n = 1
screen = pygame.display.set_mode((n*800, n*500))
pygame.display.set_caption("First Gaem")
clock = pygame.time.Clock()

bgl0 = pygame.Surface((n*800, n*500))
bgl2 = pygame.Surface((n*800, n*150))
bgl2.fill((64, 30, 1))
bgl0.fill((255, 191, 0))
bgl1 = pygame.image.load("Python/Gaem/Graphics/BG.png").convert_alpha()
bgl1 = pygame.transform.rotozoom(bgl1, 0, 0.5*n)

cactus = pygame.image.load("Python/Gaem/Graphics/cactus1.png").convert_alpha()
cactusrect = cactus.get_rect(midbottom = (n*700, n*400))

cactus2 = pygame.image.load("Python/Gaem/Graphics/cactus2.png").convert_alpha()
cactusrect2 = cactus2.get_rect(midbottom = (n*700, n*400))

dino1 = pygame.image.load("Python/Gaem/Graphics/dino1.png").convert_alpha()
dinorect1 = dino1.get_rect(midbottom = (n*80, n*400))

dino2 = pygame.image.load("Python/Gaem/Graphics/dino2.png").convert_alpha()
dinorect2 = dino2.get_rect(midbottom = (n*80, n*400))

dino3 = pygame.image.load("Python/Gaem/Graphics/dino3.png").convert_alpha()
dinorect3 = dino3.get_rect(midbottom = (n*80, n*400))

font1 = pygame.font.Font("Python/Gaem/Font/ARCADE.ttf", 30)

cntr = 0
active = True
grav = 0
speed = 7
counter = 0
stage = 0

scoreno = 0

cac = cactus
cacrec = cactusrect

while True:
    for event in pygame.event.get():  #event handler
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
        if(active == False):
            if(event.type == pygame.KEYUP):
                active = True
                cacrec.left = n*800
                cactusrect.left = n*800
                dinorect1.midbottom = (n*80, n*400)
                dinorect2.midbottom = (n*80, n*400)
                scoreno = 0
        else:
            if(event.type == pygame.KEYDOWN and (dinorect1.midbottom[1] == n*400 or dinorect2.midbottom[1] == n*400)):
                grav = -14

    if(active):
        screen.blit(bgl0, (0, 0))  #BG display
        screen.blit(bgl2, (0, n*350))
        screen.blit(bgl1, (0, n*100))

        counter += 1  #cactus
        if(counter == 600 and speed != 13):
            speed += 1
            counter = 0
        cacrec.left -= speed
        if(cacrec.right <= 0):
            rand = random.randint(1, 2)
            if(rand == 1):
                cac = cactus
                cacrec = cactusrect
            else:
                cac = cactus2
                cacrec = cactusrect2
            cacrec.left = n*800
        screen.blit(cac, cacrec)



        cntr += 1  #dino
        if(dinorect1.midbottom[1] <= n*400 or dinorect2.midbottom[1] <= n*400):
            grav += 0.5
        dinorect1.midbottom = (dinorect1.midbottom[0], dinorect1.midbottom[1]+grav)
        dinorect2.midbottom = (dinorect2.midbottom[0], dinorect2.midbottom[1]+grav)
        if(dinorect1.midbottom[1] >= n*400 or dinorect2.midbottom[1] >= n*400):
            dinorect1.midbottom = (80, n*400)
            dinorect2.midbottom = (80, n*400)
            grav = 0
        if(cntr > 15):
            screen.blit(dino1, dinorect1)
        else:
            screen.blit(dino2, dinorect2)
        if(cntr == 30):
            cntr = 0

        scoreno += 0.15#score
        score = font1.render("Score: " + str(int(scoreno)), True, "black")
        scorerect = score.get_rect(midbottom = (n*700, n*100))
        screen.blit(score, scorerect)

        if(dinorect1.colliderect(cactusrect) or dinorect2.colliderect(cactusrect)):
            active = False
        if(dinorect1.colliderect(cacrec) or dinorect2.colliderect(cacrec)):
            active = False
    else:
        screen.blit(bgl0, (0, 0))  #BG display
        screen.blit(bgl2, (0, n*350))
        screen.blit(bgl1, (0, n*100))
        screen.blit(dino3, dinorect3)
        screen.blit(cac, cacrec)
        screen.blit(cactus, cactusrect)
        screen.blit(score, scorerect)

    pygame.display.update()
    clock.tick(120)