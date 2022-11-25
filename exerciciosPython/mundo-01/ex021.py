# Tocando mp3

import pygame

pygame.init()
pygame.mixer.music.load('exerciciosPython/mundo-01/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.wait()