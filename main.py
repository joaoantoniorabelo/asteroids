# this allows us to use code from
# the open-source pygame library
# throughout this file
# PyGame support ref: https://www.pygame.org/docs/ref/pygame.html
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Pygame start
    pygame.init()
    
    # FPS
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Bind groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    
    # Asteroids
    asteroid_field = AsteroidField()
    
    # Player spawn
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # Game infinity loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   
                 
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
                
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    # end of infinity loop
    

# This line ensures the main() function is only called when this file is run directly; 
# it won’t run if it’s imported as a module. It’s considered the “pythonic” way to structure an executable program in Python. 
# Technically, the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don’t.    
if __name__ == "__main__":
    main()