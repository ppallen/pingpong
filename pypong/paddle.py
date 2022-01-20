import pygame

from asset import get_assets_dir


class Paddle:

    def __init__(self, x=20, asset='player1.png'):
        #座標
        self.x = x
        #板子長,寬,速度,生命
        self.width = 20
        self.height = 150
        self.speed = 10

        self.lives = 3

        # place paddle in the middle
        surface_height = pygame.display.get_surface().get_height()
        self.y = surface_height / 2 - self.height / 2

        self.image = pygame.image.load(
            '{}/{}'.format(get_assets_dir(), asset)
        ).convert_alpha()

    def move_up(self):
        self.y = max(self.y - self.speed, 0)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
        
>>>>>>> ad3ce87 (second)
=======

>>>>>>> a17531b (third)
=======

>>>>>>> d173cd7 (fourth)
=======
>>>>>>> 8cb9e44 (fifth)
    def move_down(self):
        surface_height = pygame.display.get_surface().get_height()
        self.y = min(self.y + self.speed, surface_height - self.height)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
