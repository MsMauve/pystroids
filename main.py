import pygame
from constants import *
from circleshape import *
from player import *
def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    Player.containers = (updatable, drawable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill((0, 0, 0))
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()
        dt = (fps_clock.tick(60)) / 1000

if __name__ == "__main__":
    main()   