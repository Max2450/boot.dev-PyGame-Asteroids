import pygame
from constants import *

def main():
    pygame.init()
    dt = 0
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        game_clock.tick(60)
        dt = game_clock.get_time() / 1000.0  # Convert milliseconds to seconds

        pygame.display.flip()

if __name__ == "__main__":
    main()
