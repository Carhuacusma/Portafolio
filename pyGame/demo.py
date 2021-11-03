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
        #Cuando el evento es presionar una tecla...
        if event.type == pygame.KEYDOWN:
            #Obtenemos el mapping de teclas presionadas
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                #Rellenamos la ventana con un color de Pygame
                window.fill(pygame.Color("blue"))
            if keys[K_a]:
                window.fill(pygame.Color("red"))
            if keys[K_d]:
                window.fill(pygame.Color("green"))
            if keys[K_q]:
                pygame.quit()
                sys.exit() # Terminar el programa    
    
        if event.type == pygame.QUIT:   
            #Si ha cerrado la ventana
            pygame.quit()
            sys.exit() # Terminar el programa
    pygame.display.flip() # Genera la ventana