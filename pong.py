import pygame, sys
from settings import *
from sprites import *


def countdown():
    if ball_1.counter == 0:
        ball_1.counter = 3
        ball_1.restart()
        ball_1.crnt_time, ball_1.scored = 0, 0
        return

    count_surf = count_font.render(f"{ball_1.counter}", True, light_grey)
    count_rect = count_surf.get_rect(center=countdown_pos)
    screen.blit(count_surf, count_rect)
    

# Game Loop
def main():
    running = True
    while running:        
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == timer:
                ball_1.counter -= 1

        # Render / Draw
        screen.fill(bg_color)
        pygame.draw.aaline(screen, grey3, scr_rect.midtop, scr_rect.midbottom)
        sprites.update()
        sprites.draw(screen)
        
        if ball_1.scored:
            countdown()


        # Update Display & Limit FPS
        pygame.display.flip()
        clock.tick(FPS)

    # Exit Game
    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()
