import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('laser4.wav')
hit_sound = pygame.mixer.Sound('Explosion+1.wav')
bg_soung = pygame.mixer.music.load('Epic Battle Trailer - AShamaluevMusic.mp3')
pygame.mixer.music.play(-1)