import pygame
import sys
running = 1

pygame.init()
while running:
	screen = pygame.display.set_mode((800, 800))
	pygame.event.get()
	pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
	pygame.QUIT
pygame.display.flip()