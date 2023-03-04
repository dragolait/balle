import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
  import pygame
import random

# Initialiser Pygame
pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définir la taille de l'écran
taille_ecran = (400, 600)
ecran = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Catch the Ball")

# Définir la position initiale de la balle
position_balle = [random.randint(0, taille_ecran[0]), 0]

# Définir la taille de la balle et sa vitesse
taille_balle = 50
vitesse_balle = 5

# Définir la position initiale du joueur
position_joueur = [taille_ecran[0]//2, taille_ecran[1]-50]

# Définir la taille du joueur
taille_joueur = [50, 50]

# Boucle principale
continuer = True
while continuer:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    # Dessiner l'écran
    ecran.fill(BLANC)

    # Dessiner la balle
    pygame.draw.circle(ecran, NOIR, position_balle, taille_balle)

    # Déplacer la balle vers le bas
    position_balle[1] += vitesse_balle

    # Vérifier si la balle touche le sol
    if position_balle[1] > taille_ecran[1]:
        position_balle = [random.randint(0, taille_ecran[0]), 0]

    # Dessiner le joueur
    pygame.draw.rect(ecran, NOIR, [position_joueur[0], position_joueur[1], taille_joueur[0], taille_joueur[1]])

    # Mettre à jour l'écran
    pygame.display.flip()

    # Obtenir la position du doigt du joueur
    position_doigt = pygame.mouse.get_pos()

    # Mettre à jour la position du joueur
    position_joueur[0] = position_doigt[0]

    # Vérifier si le joueur attrape la balle
    if position_balle[1] + taille_balle > position_joueur[1] and position_balle[0] > position_joueur[0] and position_balle[0] < position_joueur[0] + taille_joueur[0]:
        position_balle = [random.randint(0, taille_ecran[0]), 0]

# Quitter Pygame
pygame.quit()
