import pygame
from constants import *
from player import Player

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2



def main() :
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(x,y)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0

    while True :
        screen.fill("black")
        player.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) /1000   
            
        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
     
    
   












if __name__ == "__main__":
    main()