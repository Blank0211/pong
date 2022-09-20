import os
import pygame
from my_funcs import to_rgb

# Font
pygame.font.init()
roboto1 = os.path.join('assets', 'Roboto-Regular.ttf')
my_font = pygame.font.Font(roboto1, 26)
count_font = pygame.font.Font(roboto1, 34)

# Sounds Effects
pygame.mixer.init()
pong_path = os.path.join('assets', 'pong.ogg')
score_path = os.path.join('assets', 'score.ogg')
pong_se = pygame.mixer.Sound(pong_path)
score_se = pygame.mixer.Sound(score_path)


# Colours
cyan = to_rgb('#008b92')
light_cyan = to_rgb('#9fcad6')
dark_cyan = to_rgb('#00404a')
dark_green = to_rgb('#002324')
sandy = to_rgb('#d4cbc2')
sandy_2 = to_rgb('#adaa9d')
light_grey = to_rgb('#d9e0e9')
grey3 = to_rgb('7686a6')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen & Background Settings
WIDTH = 800
HEIGHT = 500
FPS = 60
bg_color = dark_cyan

# Paddle & Ball Settings
pad_color = light_cyan
ball_color = sandy_2

player_speed = 6
ai_speed = 5
ball_speed = None

pad_width = 10
pad_height = 90

# Score
score1_pos = ((WIDTH//2) + 30, 10) # Right to mid
score2_pos = ((WIDTH//2) - 30, 10) # Left to mid

countdown_pos = (WIDTH//2, (HEIGHT//2) + 50)
