import pygame, os
import random
from ElementGraphique import ElementGraphique


class Balle(ElementGraphique):
    def __init__(self, img, fen):
        largeur, hauteur = fen.get_size()
        temp = img.get_rect()
        x = random.randint(0, largeur-temp.w)
        y = random.randint(0, hauteur-temp.h)
        ElementGraphique.__init__(self, img, fen, x,y)
        dx = random.randint(-10,10)
        dy = random.randint(-10,10)
        self.dx = dx
        self.dy = dy 

    def deplacer(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        largeur, hauteur = self.fen.get_size()
        if (self.rect.y < 0 or self.rect.y + self.rect.h > hauteur) :
            self.dy = -self.dy
        if (self.rect.x < 0 or self.rect.x + self.rect.w > largeur):
            self.dx = -self.dx

    def apparence(self, other):
        if self.collide(other):
            self.image =  pygame.transform.scale(pygame.image.load(os.path.join('ball_states', 'ball3.png')), (40,40))
            self.afficher()

