import pygame, os, time
from ElementGraphique import ElementGraphique
from Perso import Perso
from Balle import Balle


# Initialisation de la bibliotheque pygame
pygame.init()

#creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))


# lecture de l'image du perso
imagePerso = pygame.image.load("perso.png")

perso = Perso(imagePerso,fenetre,60,80, True, 3)


# lecture de l'image du fond
imageFond = pygame.image.load("background.png").convert()
fond = ElementGraphique(imageFond,fenetre,0,0)

## Ajoutons un texte fixe dans la fenetre :
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)
score = 1000
# Creation de l'image correspondant au texte
imageText = font.render('<Escape> pour quitter : '+str(score), True, (255, 0, 255))

# creation d'un rectangle pour positioner l'image du texte
texte = ElementGraphique(imageText,fenetre,10,10)
DEFAULT_IMAGE_SIZE = (40, 40)
imageBalle = pygame.transform.scale(pygame.image.load(os.path.join('ball_states', 'ball1.png')), DEFAULT_IMAGE_SIZE)

balls = []

balle = Balle(imageBalle,fenetre)
balls.append(balle)




# counter = 0



# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle dont on veut sortir :
#   - en appuyant sur ESCAPE
#   - en cliquant sur le bouton de fermeture
i=1;
global continuer
continuer = 1
while continuer:

    # fixons le nombre max de frames / secondes
    horloge.tick(30)

    i=i+1
    #print (i)

    if (i%90 == 0 and len(balls) < 4):
        balle = Balle(imageBalle,fenetre)
        balls.append(balle)

        

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=0

    for b in balls:
        b.deplacer()
        

    # Affichage du fond
    fond.afficher()

    # Affichage Perso
    perso.afficher()

    for b in balls:
        b.afficher()
        b.apparence(perso)
        

    # Affichage du Texte
    texte.afficher()

    perso.deplacer()
    
    # Gestion des vies
    perso.health(balls)
    for b in balls:
        if perso.pv == 0:
            if (perso.collide(b)):
                continuer = 0


    # rafraichissement
    pygame.display.flip()

    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
            continuer = 0	   # On arrete la boucle

# fin du programme principal...
pygame.quit()
