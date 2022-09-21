import os
import pygame
from my_funcs import to_rgb


# Colours
light_grey = to_rgb('#d9e0e9')
grey3 = to_rgb('7686a6')
red1 = to_rgb('#2F373F')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen & Background Settings
WIDTH = 800
HEIGHT = 500
FPS = 120
bg_color = red1

# General Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
scr_rect = screen.get_rect()
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

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

# Paddle & Ball Settings
paddle_img = os.path.join('assets', 'Paddle.png')
ball_img = os.path.join('assets', 'Ball.png')

player1_speed = 6
player2_speed = 5
ball_speed = None

pad_width = 10
pad_height = 90

# Score
score1_pos = ((WIDTH//2) + 30, 10) # Right to mid
score2_pos = ((WIDTH//2) - 30, 10) # Left to mid

countdown_pos = (WIDTH//2, (HEIGHT//2) + 50)
