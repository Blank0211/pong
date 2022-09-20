import random


import pygame


from settings import *



# Classes and instances for sprites
class SpriteGroup():
    """Class for managing sprite objects"""
    def __init__(self, *sprite_objs):
        self.sprite_list = []
        for sprite in sprite_objs:
            self.sprite_list.append(sprite)

    def add(self, sprite_obj):
        self.sprite_list.append(sprite_obj)

    def update(self, *args):
        for sprite in self.sprite_list:
            sprite.update(*args)

    def draw(self, screen):
        for sprite in self.sprite_list:
            screen.blit(sprite.image, sprite.rect)


timer = pygame.USEREVENT # TODO: Find a better place for timer
class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, pos_x, pos_y):
        super().__init__()
        
        self.image = pygame.Surface((radius*2, radius*2))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        pygame.draw.circle(self.image, ball_color, (radius, radius), radius)
        self.image.set_colorkey(BLACK)

        self.vel_x = 5
        self.vel_y = 5

        # Setup for countdown
        self.scored = None
        self.crnt_time = None
        self.counter = 3

    def restart(self):
        self.crnt_time = pygame.time.get_ticks()

        if (self.rect.left < 0):
            score1.increase()
        if (self.rect.right > WIDTH):
            score2.increase()
        
        # Keep the ball paused until countdown is finished
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.vel_x, self.vel_y = 0, 0
        if self.crnt_time - self.scored > 2100:
            self.vel_x = 5
            self.vel_y = 5
            self.vel_x *= random.choice([1, -1])
            self.vel_y *= random.choice([1, -1])

    def update(self, *args):
        # Collsion with right player
        if self.rect.colliderect(paddle_1.rect) and self.vel_x > 0:
            pong_se.play() # Sound Effect

            if abs(self.rect.right - paddle_1.rect.left) < 10:
                self.vel_x *= -1
            elif (abs(self.rect.bottom - paddle_1.rect.top) < 10 and
                  self.vel_y > 0):
                self.vel_y *= -1
            elif (abs(self.rect.top - paddle_1.rect.bottom) < 10 and
                  self.vel_y < 0):
                self.vel_y *= -1
        
        # Collision with left player
        if self.rect.colliderect(paddle_2.rect) and self.vel_x < 0:
            pong_se.play() # Sound Effect

            if abs(self.rect.left - paddle_2.rect.right) < 10:
                self.vel_x *= -1
            elif (abs(self.rect.bottom - paddle_2.rect.top) < 10 and
                  self.vel_y > 0):
                self.vel_y *= -1
            elif (abs(self.rect.top - paddle_2.rect.bottom) < 10 and
                  self.vel_y < 0):
                self.vel_y *= -1

        # Collision with boundaries
        if (self.rect.top <= 0) or (self.rect.bottom >= HEIGHT):
            self.vel_y *= -1
        if (self.rect.left < 0) or (self.rect.right > WIDTH):
            score_se.play() # Sound Effect
            # Setup for restart & countdoun
            self.scored = pygame.time.get_ticks()
            pygame.time.set_timer(timer, 700, 3)
            self.restart()

        # Ball movement
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class Player(pygame.sprite.Sprite):
    """Class representing right player's paddle"""
    def __init__(self, speed, **pos):
        super().__init__()

        self.image = pygame.Surface((pad_width, pad_height))
        self.image.fill(pad_color)
        self.rect = self.image.get_rect(**pos)

        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()

        # Move up and down
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed


class AiPlayer(pygame.sprite.Sprite):
    """Class representing left player's paddle"""
    def __init__(self, speed, **pos):
        super().__init__()

        self.image = pygame.Surface((pad_width, pad_height))
        self.image.fill(pad_color)
        self.rect = self.image.get_rect(**pos)

        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()

        # Move up and down
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


class Score():

    # Set score surface and position
    def __init__(self, score_pos):
        self.num = 0
        self.image = my_font.render(f'{self.num}', True, light_grey)
        self.rect = self.image.get_rect(midtop=score_pos)

    # Increment score
    def increase(self):
        self.num += 1
        self.image = my_font.render(f'{self.num}', True, light_grey)

    def update(self):
        pass

            




# ------ Sprite Instances ------

# Set up right paddle
paddle_1 = Player(player_speed, midright=(795, HEIGHT//2))

# Set up left paddle
paddle_2 = AiPlayer(ai_speed, midleft=(5, HEIGHT//2))

# Set up ball in middle
ball_1 = Ball(14, WIDTH//2, HEIGHT//2)

score1 = Score(score1_pos) # Left score
score2 = Score(score2_pos) # Right score

# Group all sprites
sprites = SpriteGroup(ball_1, paddle_1, paddle_2, score1, score2)

