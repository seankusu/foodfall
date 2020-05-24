import pygame

def main():
    pygame.init()
    width = 500
    height = 500
    win = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Food Fall')
    
    x1 = 300
    y1 = 300
    
    x1_change = 0       
    y1_change = 0
    
    clock = pygame.time.Clock()
    
    game_over = False
    while not game_over:    
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                game_over = True
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

    pygame.quit()
    quit()
main()