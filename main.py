# this allows us to use code from
# the open-source pygame library
# throughout this file
# PyGame support ref: https://www.pygame.org/docs/ref/pygame.html
import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Pygame start
    pygame.init()
    
    # FPS
    clock = pygame.time.Clock()
    dt = 0
    
    # Player spawn
    player_x = SCREEN_WIDTH/2 # center screen x
    player_y = SCREEN_HEIGHT/2 # center screen y
    player = Player(player_x, player_y)
    
    # Group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Bind groups to Player
    Player.containers = (updatable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game infinity loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   
                 
        updatable.update(dt)
        
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