#Faça um progrma em python que abra e reproduza o audio de um arquivo MP3

import pygame

pygame.init()

pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
