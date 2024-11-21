import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfeild import AsteroidField
from shoot import Shoot

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2



def main() :
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoot = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shoot.containers = (shoot,drawable,updatable)
    asteroid_field = AsteroidField()                    

    player = Player(x,y)

    dt = 0

    while True :
        for item in updatable :
            item.update(dt)
        for item in asteroids:
            if item.collisions(player):
                print("Game Over!")
                raise SystemExit
        screen.fill("black")
        for item in drawable:
            item.draw(screen)

            

        
        pygame.display.flip()
        
        dt = clock.tick(60) /1000   
            
        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
     
    
   












if __name__ == "__main__":
    main()