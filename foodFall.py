import pygame
import random
pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Food Fall')

def dropSushi(x,speed):
    width = 40
    height = 60
    sushi1Img = pygame.image.load('sushi1.png')
    sushi1Img = pygame.transform.scale(sushi1Img, (width, height))
    
    y = 0
    while y <= 440:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        win.blit(sushi1Img, (x,y))
        pygame.display.update()
        pygame.draw.rect(win, (0,0,0), (x, y , width, height))
        y+= speed

def main():
    x1 = 300
    y1 = 300
    
    x1_change = 0       
    y1_change = 0
    
    clock = pygame.time.Clock()
        
    count = 0
    speed = 3
    
    
    run = True
    while run:
        surf = pygame.Surface((550,550))
        #surf.fill((0,255,0))
        x1 += x1_change
        y1 += y1_change
        
        center = (x1,y1)
        radius = 40
        pygame.draw.circle(surf, (0,0,255), center, radius)
        win.blit(surf, (-50,190))
        pygame.display.update()
        
        clock.tick(30)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                run = False
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x1_change = 0
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 0
                    y1_change = 0
        
        pygame.time.delay(100)
        x = random.randint(0,460)
        color1 = random.randint(0,255)
        color2 = random.randint(0,255)
        color3 = random.randint(0,255)
        
        dropSushi(x, speed)
        #dropFood(x + 40, speed, color1, color2, color3)
        count += 1
        if count == 10:
            speed += .1

    pygame.quit()
    quit()
    
main()