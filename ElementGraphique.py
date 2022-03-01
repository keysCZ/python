import pygame, os

class ElementGraphique():
    def __init__(self, img, fen, x,y):
        self.image = img
        self.rect = img.get_rect()
        self.fen = fen
        self.rect.x = x
        self.rect.y = y

    def afficher(self):
        self.fen.blit(self.image, self.rect)

    

    def collide(self,other):
        if self.rect.colliderect(other.rect):
            return True
        return False

