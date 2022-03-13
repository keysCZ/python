import pygame, os
import random
from ElementGraphique import ElementGraphique
# timer, self.touchee = True, images, deplacer : if self.touchee ==True  
class Balle(ElementGraphique):
    def __init__(self, imgs, fen, touchee):
        self.imgs = imgs
        self.touchee = touchee
        self.timer = 0 
        self.image = pygame.transform.scale(pygame.image.load(self.imgs[0]), (60,60))
        largeur, hauteur = fen.get_size()
        temp = self.image.get_rect()
        x = random.randint(0, largeur-temp.w)
        y = random.randint(0, hauteur-temp.h)
        ElementGraphique.__init__(self, self.image, fen, x,y)
        dx = random.randint(-10,10)
        dy = random.randint(-10,10)
        self.dx = dx
        self.dy = dy 

    def deplacer(self):
        self.timer+=1

        self.rect.x += self.dx
        self.rect.y += self.dy
        largeur, hauteur = self.fen.get_size()
        if (self.rect.y < 0 or self.rect.y + self.rect.h > hauteur) :
            self.dy = -self.dy
        if (self.rect.x < 0 or self.rect.x + self.rect.w > largeur):
            self.dx = -self.dx

        if self.timer>30: 
            self.touchee=False 
            self.image = pygame.transform.scale(pygame.image.load(self.imgs[0]), (60,60))

    def toucher(self, other):
        if self.collide(other):
            self.touchee = True
            self.image =  pygame.transform.scale(pygame.image.load(self.imgs[1]), (60,60))
            self.afficher()

    

