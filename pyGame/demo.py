import pygame
from pygame.locals import * # Necesario para teclado
import sys

pygame.init()

#Establecemos el tamaño de la ventana.
window = pygame.display.set_mode((700,400)) # https://www.pygame.org/docs/ref/display.html
pygame.display.set_caption("Demo")

#Bucle
while True:
    for event in pygame.event.get():
        #Por cada 'evento'
        if event.type == pygame.QUIT:   
            #Si ha cerrado la ventana
            pygame.quit()
            sys.exit() # Terminar el programa
    pygame.display.flip() # Genera la ventana