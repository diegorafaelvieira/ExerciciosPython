# DESAFIO 021
# Faça um programa Python que abra e reproduza o áudio de um arquivo mp3
import pygame  # NECESSÁRIO INSTALAR O PACKAGE PYGAME
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()