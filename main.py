import pygame 
from constants import *
pygame.init
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            pygame.quit()
        screen.fill("black")
        pygame.display.flip()




#def main():
#    print("Starting Asteroids!")
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")

#if __name__ == "__main__":
#    main()
