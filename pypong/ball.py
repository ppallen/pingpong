import pygame
import numpy as np

from asset import get_assets_dir
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d173cd7 (fourth)

=======
>>>>>>> 8cb9e44 (fifth)
class Ball:

    def __init__(self):
        self.width = 20
        self.height = 20

        self.position = self._initial_position()
<<<<<<< HEAD
        self.acceleration = np.array([5, 1])

<<<<<<< HEAD
=======
class Ball:

    def __init__(self,x):
        self.x = x
        self.width = 20
        self.height = 20

        self.position = (self._initial_position(-350,10))
        self.acceleration = np.array([x, 1])
        
>>>>>>> ad3ce87 (second)
=======
class Ball:

    def __init__(self,x,check):
        self.x = x
        self.width = 20
        self.height = 20
        self.c=check
        self.position = (self._initial_position(-350))
        self.acceleration = np.array([x, 1])
        
>>>>>>> a17531b (third)
=======
>>>>>>> d173cd7 (fourth)
        self.image = pygame.image.load(
            '{}/ball.png'.format(get_assets_dir())
        ).convert_alpha()

=======
        self.acceleration = np.array([40, 1])
        
        self.image = pygame.image.load(
            '{}/ball.png'.format(get_assets_dir())
            ).convert_alpha()
>>>>>>> 8cb9e44 (fifth)
    def accelerate(self, factor):
        self.acceleration = np.multiply(self.acceleration, np.array([-1, 1]))
        self.acceleration[1] = factor

    def acceleration_multiply(self, vector):
        self.acceleration = np.multiply(self.acceleration, vector)

    def draw(self, surface):
        surface.blit(self.image, (self.position[0], self.position[1]))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d173cd7 (fourth)
    def reset(self):
        self.position = self._initial_position()
        self.acceleration = np.array([5, 1])

    def _initial_position(self):
<<<<<<< HEAD
=======
    def reset(self,First_Player,Second_Player):
        if First_Player:
            self.position = self._initial_position(-350,10)
            First_Player = False
        if Second_Player:
            self.position = self._initial_position(350,10)
            Second_Player = False
        self.acceleration = np.array([self.x, 1])

    def _initial_position(self,start_x,start_y):
>>>>>>> ad3ce87 (second)
=======
    def reset(self,First_Player,Second_Player):
        if First_Player:
            self.position = self._initial_position(-350)
            First_Player = False
        if Second_Player:
            self.position = self._initial_position(350)
            Second_Player = False
        self.acceleration = np.array([self.x, 1])

    def _initial_position(self,start_x):
>>>>>>> a17531b (third)
=======
>>>>>>> d173cd7 (fourth)
=======
    def reset(self):
        self.position = self._initial_position()
        self.acceleration = np.array([20, 1])
    def _initial_position(self):
>>>>>>> 8cb9e44 (fifth)
        # place ball in the middle
        surface_width = pygame.display.get_surface().get_width()
        surface_height = pygame.display.get_surface().get_height()

        return np.array([
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            surface_width / 2 - self.width / 2,
            surface_height / 2 - self.height / 2
        ])
=======
            surface_width / 2 - self.width / 2 + start_x,
            surface_height / 2 - self.height / 2 
        ])
        
        
>>>>>>> ad3ce87 (second)
=======
            surface_width / 2 - self.width / 2 + start_x,
            surface_height / 2 - self.height / 2
        ])
>>>>>>> a17531b (third)
=======
            surface_width / 2 - self.width / 2,
            surface_height / 2 - self.height / 2
        ])
>>>>>>> d173cd7 (fourth)
=======
            surface_width / 2 - self.width / 2,
            surface_height / 2 - self.height / 2
        ])
>>>>>>> 8cb9e44 (fifth)
