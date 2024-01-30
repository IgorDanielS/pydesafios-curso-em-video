#Desafio: Rodar alguma música utilizando o python.

import pygame

pygame.init()
file = 'LegiãoUrbana.mp3'
pygame.mixer.music.load(file)
pygame.mixer.music.play()

#Utilizei esse input de forma intuitiva para que o código não pare antes da música acabar, caso contrário o código para antes da música finalizar
#Outra alternativa seria usar o time.sleep(), mas aí teria que calcular o tamanho da música e colocar como parâmetro, nesse sentido, fica mais 
#fácil utilizar esse método do inputEspera
inputEspera = input('Tocando a musica...')

