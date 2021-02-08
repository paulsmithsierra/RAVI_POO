import random
import pygame
from pygame.math import Vector2


class Drop:
    def __init__(self, largeur):
      self.gravity = random.randint(5,20)
      self.size = random.randint(5,10)
      self.R = random.randint(0,255)
      self.G = random.randint(0,255)
      self.B = random.randint(0,255)
      self.position = Vector2(random.randint(0,largeur), random.randint(-200,0))
    #-200 permet de faire la creation des gouttes en dehors de l'ecran

    def tomber(self, hauteurFenetre):
        self.position.y = self.position.y + self.gravity
        if self.position.y > hauteurFenetre:
            self.raz()

    def raz(self):
        self.position.y = 0

    def afficher(self, core):
        pygame.draw.line(core.screen, (self.R, self.G, self.B), (self.position.x, self.position.y), (self.position.x, self.position.y + self.size), 1)
