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

# Match Countdoun
def countdown():
    counter = 3
    my_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(my_timer, 1000)

    text_surf = count_font.render(f"{counter}", True, light_grey)
    text_rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
        
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == my_timer:
                counter -= 1

        text_surf = count_font.render(f"{counter}", True, dark_green)
        screen.blit(text_surf, text_rect)
        if counter < 1:
            running = False

        pygame.display.flip()



# Game Loop
def main():
    running = True
    while running:        
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == score_event:
                countdown()
        keys = pygame.key.get_pressed()

        # Render / Draw
        screen.fill(bg_color)
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
