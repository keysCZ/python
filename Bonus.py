import pygame
import os
import random
from ElementGraphique import ElementGraphique
# timer, self.touchee = True, images, deplacer : if self.touchee ==True


class Bonus(ElementGraphique):
    def __init__(self, imgs, fen, touchee):
        self.imgs = imgs
        self.touchee = touchee
        self.timer = 0
        self.img = random.choices(self.imgs, weights=(50,50,0,0), k=1)
        self.image = pygame.transform.scale(
            pygame.image.load(self.img[0]), (30, 30))
        temp = self.image.get_rect()
        largeur, hauteur = fen.get_size()
        x = random.randint(0, largeur-temp.w)
        y = random.randint(0, hauteur-temp.h)
        ElementGraphique.__init__(self, self.image, fen, x, y)
        dx = 0
        dy = random.randint(0, 10)
        self.dx = dx
        self.dy = dy

    def deplacer(self):
        self.timer += 1
        self.rect.x += self.dx
        self.rect.y += self.dy
    

    def toucher(self, perso):
        if self.collide(perso):
            self.touchee = True
            self.img = self.imgs[3]
            self.image = pygame.image.load(
                os.path.join('Magic Pixel Art', self.imgs[3]))
            self.afficher()
