from itertools import count
import pygame
import os
from Balle import Balle
from ElementGraphique import ElementGraphique


class Perso(ElementGraphique):
    def __init__(self, img, fen, x, y, invulnerability, pv):
        self.invulnerability = invulnerability
        self.rapidity = False
        self.pv = pv
        self.counter = 0
        ElementGraphique.__init__(self, img, fen, x, y)

    def deplacer(self, k):
        largeur, hauteur = self.fen.get_size()
        # on recupere l'etat du clavier
        touches = pygame.key.get_pressed()

        if (touches[pygame.K_LEFT]):
            self.rect.x -= k
        if (touches[pygame.K_RIGHT]):
            self.rect.x += k
        if (touches[pygame.K_UP]):
            self.rect.y -= k
        if (touches[pygame.K_DOWN]):
            self.rect.y += k
        if (self.rect.x < 0):
            self.rect.x = 0
        if (self.rect.x + self.rect.w > largeur):
            self.rect.x = largeur - self.rect.w
        if (self.rect.y < 0):
            self.rect.y = 0
        if (self.rect.y + self.rect.h > hauteur):
            self.rect.y = hauteur - self.rect.h

        if self.invulnerability == True or self.rapidity == True :
            self.counter = self.counter + 1
            # print(self.counter)


    ### HEALTH ###

    def health(self):
        if self.pv == 3:
            imgLife = pygame.image.load(os.path.join(
                'heart pixel art', 'heart pixel art 48x48.png'))
            life = ElementGraphique(imgLife, self.fen, 500, 20)
            life.afficher()

        if self.pv == 2:
            imgLife = pygame.image.load(os.path.join(
                'heart pixel art', 'heart pixel art 32x32.png'))
            life = ElementGraphique(imgLife, self.fen, 500, 20)
            life.afficher()
        if self.pv == 1:
            imgLife = pygame.image.load(os.path.join(
                'heart pixel art', 'heart pixel art 16x16.png'))
            life = ElementGraphique(imgLife, self.fen, 500, 20)
            life.afficher()

       

    def appliquer_degats(self, other):
        font = pygame.font.Font(None, 34)
        if self.counter == 30:
            self.invulnerability = False
            self.counter = 0
        if (self.collide(other)):
            if self.invulnerability == False:
                self.pv = self.pv - 1
                print(self.pv)

            self.invulnerability = True
            self.counter = 0
        # print(self.invulnerability)


    ### BONUS ###

    def bonus_pv(self, bonus):
        if (self.collide(bonus)):
            if self.pv < 3:
                self.pv = self.pv + 1
                self.invulnerability = True
                self.counter = 0
                print(self.pv)

    def bonus_rapidity(self, bonusR):
        if self.counter == 30:
            self.rapidity = False
            self.counter = 0
        if (self.collide(bonusR)):
            self.rapidity = True
            self.counter = 0

