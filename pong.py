import pygame, sys
from settings import *
from sprites import *
from my_funcs import natural_sort as natsort

# General Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
scr_rect = screen.get_rect()
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()


# Game Loop
def main():
    running = True
    while running:        
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        # Render / Draw
        screen.fill(bg_color)
        screen.blits(scores_info)
        pygame.draw.aaline(screen, grey3, scr_rect.midtop, scr_rect.midbottom)
        sprites.update()
        sprites.draw(screen)

        # Update Display & Limit FPS
        pygame.display.flip()
        clock.tick(FPS)

    # Exit Game
    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()
