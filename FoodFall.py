import pygame
import random
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Food Fall")

#this is mias change
#sushi1Img = pygame.image.load('sushi1.png')


def Sushi(x,y):
    gameDisplay.blit(sushi1Img, (x,y))

def dropSushi(x,speed, count):
    width = 40
    height = 60
    y = 0
    while y <= 440:
        pygame.draw.rect(win, (color1, color2, color3), (x, y , width, height))
        pygame.display.update()
        pygame.draw.rect(win, (0,0,0), (x, y , width, height))
        y+=speed
 
def dropFood(x,speed,color1, color2, color3):
    width = 40
    height = 60
    y = 0
    while y <= 440:
        pygame.draw.rect(win, (color1, color2, color3), (x, y , width, height))
        pygame.display.update()
        pygame.draw.rect(win, (0,0,0), (x, y , width, height))
        y+=speed

def main():
    count = 0
    speed = .2
    
    run = True
    while run:
        pygame.time.delay(100)
        x = random.randint(0,460)
        color1 = random.randint(0,255)
        color2 = random.randint(0,255)
        color3 = random.randint(0,255)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                run = False
                
        dropFood(x, speed, color1, color2, color3)
        count += 1
        if count == 10:
            speed += .1
    
    pygame.quit()
    quit()
    
main()
