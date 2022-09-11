# Classes and instances for sprites
from settings import *
import pygame

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


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, pos_x, pos_y):
        super().__init__()
        
        self.image = pygame.Surface((radius*2, radius*2))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        pygame.draw.circle(self.image, ball_color, (radius, radius), radius)
        self.image.set_colorkey(BLACK)

        self.vel_x = 5
        self.vel_y = 5

    def update(self, *args):
        if self.rect.colliderect(paddle_1.rect):
            self.vel_x *= -1
        if self.rect.colliderect(paddle_2.rect):
            self.vel_x *= -1

        if (self.rect.top <= 0) or (self.rect.bottom >= HEIGHT):
            self.vel_y *= -1
        if (self.rect.left < 0) or (self.rect.right > WIDTH):
            self.vel_x *= -1

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y





class Player(pygame.sprite.Sprite):
    """Class representing player's paddle"""
    def __init__(self, speed, **pos):
        super().__init__()

        self.image = pygame.Surface((pad_width, pad_height))
        self.image.fill(pad_color)
        self.rect = self.image.get_rect(**pos)

        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed


class AiPlayer(pygame.sprite.Sprite):
    """Class representing player's paddle"""
    def __init__(self, speed, **pos):
        super().__init__()

        self.image = pygame.Surface((pad_width, pad_height))
        self.image.fill(pad_color)
        self.rect = self.image.get_rect(**pos)

        self.speed = speed

    def update(self):
        if self.rect.top >= ball_1.rect.top:
            self.rect.y -= self.speed
        if self.rect.bottom <= ball_1.rect.bottom:
            self.rect.y += self.speed

            




# ------ Sprite Instances ------

# Place player paddle in mid right of screen
paddle_1 = Player(player_speed, midright=(795, HEIGHT//2))

# Place AI paddle in mid left of screen
paddle_2 = AiPlayer(ai_speed, midleft=(5, HEIGHT//2))

# Place ball in the middle of screen
ball_1 = Ball(14, WIDTH//2, HEIGHT//2)

sprites = SpriteGroup(ball_1, paddle_1, paddle_2)

