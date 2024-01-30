import pygame

pygame.init()
file = 'LegiãoUrbana.mp3'
pygame.mixer.music.load(file)
pygame.mixer.music.play()

inputEspera = input('Tocando a musica...')

