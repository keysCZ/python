from itertools import count
import pygame, os
from Balle import Balle
from ElementGraphique import ElementGraphique

class Perso(ElementGraphique):
    def __init__(self, img, fen, x,y, invulnerability, pv):
        self.invulnerability = invulnerability
        self.pv = pv
        self.counter = 0
        ElementGraphique.__init__(self, img, fen, x,y)
        
    def deplacer(self):
        largeur, hauteur = self.fen.get_size()
        # on recupere l'etat du clavier
        touches = pygame.key.get_pressed();

        if (touches[pygame.K_LEFT]):
            self.rect.x -= 5
        if (touches[pygame.K_RIGHT]):
            self.rect.x += 5
        if (touches[pygame.K_UP]):
            self.rect.y -= 5
        if (touches[pygame.K_DOWN]):
            self.rect.y += 5
        if (self.rect.x < 0):
            self.rect.x = 0
        if (self.rect.x + self.rect.w > largeur):
            self.rect.x = largeur - self.rect.w
        if (self.rect.y < 0):
            self.rect.y = 0
        if (self.rect.y + self.rect.h > hauteur):
            self.rect.y = hauteur - self.rect.h
       
        if self.invulnerability == True : 
            self.counter = self.counter + 1
            #print(self.counter)

    def appliquer_degats(self, other):
        font = pygame.font.Font(None, 34)
        if self.counter == 30:
                self.invulnerability = False
                self.counter = 0
        if (self.collide(other)):
            if self.invulnerability == False :
                self.pv = self.pv - 1
                # imagePV = font.render('PV : '+str(self.pv), True, (255, 0, 0))
                # health = ElementGraphique(imagePV,self.fen,500,10)
                # health.afficher()
            self.invulnerability = True
            self.counter = 0
        #print(self.invulnerability)

    def health(self, other):
        for e in other:
            if self.pv == 3:
                imgLife = pygame.image.load(os.path.join('heart pixel art', 'heart pixel art 48x48.png'))
                life = ElementGraphique(imgLife,self.fen,500,20)
                life.afficher()
            self.appliquer_degats(e)
            if self.pv == 2:
                imgLife = pygame.image.load(os.path.join('heart pixel art', 'heart pixel art 32x32.png'))
                life = ElementGraphique(imgLife,self.fen,500,20)
                life.afficher()
            if self.pv == 1:
                imgLife = pygame.image.load(os.path.join('heart pixel art', 'heart pixel art 16x16.png'))
                life = ElementGraphique(imgLife,self.fen,500,20)
                life.afficher()
            

        





