import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    dt = 0
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
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
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
