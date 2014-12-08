import pygame
from pygame.locals import *
# Constants for keys pressed is something like K_A

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 225, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill(black)
pygame.draw.rect(screen, green, (0, 0, 50, 50))

while True:
	event = pygame.event.poll()
	pygame.display.update()  # redraw the screen
	pygame.time.delay(500)