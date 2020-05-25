import pygame
import random
pygame.init()

def movingMouth(win, turn = "mouth", x = 300, y = 300):
    def drawMouth(x, y):
        surf = pygame.Surface((550,550))
        #surf.fill((0,255,0))

        center = (x,y)
        radius = 40
        pygame.draw.circle(surf, (0,0,255), center, radius)
        win.blit(surf, (-50,190))
        
        pygame.display.update

    speed = 3
    x_change = 0
    y_change = 0

    run = True
    while run:
        print ("it's %s" % (turn))

        try:
            drawMouth(x, y)

            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -15
                        y_change = 0
                        print("moved x by %d" % x_change)
                    elif event.key == pygame.K_RIGHT:
                        x_change = 15
                        y_change = 0
                        print("moved x by %d" % x_change)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        x_change = 0
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = 0
                        y_change = 0

            x += x_change
            y += y_change

            drawMouth(x, y)
            print("new %s position (x,y) <=> (%d, %d)" % (turn, x, y))

        except:
            println("encountering failure")
        
        print("exiting %s" % turn)
        yield

def droppingSushi(win, turn = "sushi"):

    def dropSushi(x,speed,y_change_min,y_change_max):
        width = 40
        height = 60
        sushi1Img = pygame.image.load('sushi1.png')
        sushi1Img = pygame.transform.scale(sushi1Img, (width, height))

        y = y_change_min
        while y >= y_change_min and y <= y_change_max:
            print("%d : dropping sushi position (y_min, y_max) => (%d, %d)" % (y, y_change_min, y_change_max))
            win.blit(sushi1Img, (x,y))
            pygame.display.update()
            pygame.draw.rect(win, (0,0,0), (x, y , width, height))
            y+= speed
        
    speed = .3

    y_change = 100
    y_min = 0
    y_max = 400
    y_change_min = 0
    y_change_max = 0

    run = True
    while run:
        print ("it's %s" % (turn))
        #pygame.time.delay(100)
        if y_change_min == y_min or y_change_max == y_max:
            x = random.randint(0,460)
            color1 = random.randint(0,255)
            color2 = random.randint(0,255)
            color3 = random.randint(0,255)
        
        try:
            if y_change_max == y_max:
                y_change_max = y_min
            y_change_min = y_change_max
            y_change_max = y_change_min + y_change
            dropSushi(x, speed, y_change_min, y_change_max)
            #dropFood(x + 40, speed, color1, color2, color3)
        except:
            println("encountering failure")

        print("exiting %s" % turn)
        yield

def main():
    width = 500
    height = 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Food Fall')

    clock = pygame.time.Clock()

    mouth_x = 300
    mouth_y = 300

    try:
        turn = "start"
        mouth = movingMouth(win, "mouth")
        sushi = droppingSushi(win, "sushi")

        count = 0
        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
            count+=1
            print("%d : moved mouth to new position (x,y) => (%d,%d)" % (count, mouth_x, mouth_y))
            state = sushi
            print(state)
            next(state)
            state = mouth
            print(state)
            next(state)
            pygame.display.update()
    except:
        println("I am done - quitting.")
    finally:
        pygame.quit()
        quit()
    
main()