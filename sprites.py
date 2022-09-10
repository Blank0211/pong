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


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, pos_x, pos_y):
        self.image = pygame.Surface((radius*2, radius*2))
        pygame.draw.circle(self.image, light_cyan, radius)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect(center=(pos_x, pos_y))

