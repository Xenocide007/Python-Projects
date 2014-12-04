mouseCO = "Mario.png"
bg = "bg.png"

import pygame, sys
from pygame.locals import *

pygame.init()
fps = 30

screen = pygame.display.set_mode((1280, 1280), 0, 32)

background = pygame.image.load(bg).convert()
mouseC = pygame.image.load(mouseCO).convert_alpha()

x, y = 0,0
movex, movey = 0, 0

isAlive = 'yes'

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				movex = -10
			elif event.key == K_RIGHT:
				movex = +10
			elif event.key == K_UP:
				movey = -10
			elif event.key == K_DOWN:
				movey = +10
		if event.type == KEYUP:
			if event.key == K_LEFT:
				movex = 0
			elif event.key == K_RIGHT:
				movex = 0
			elif event.key == K_UP:
				movey = 0
			elif event.key == K_DOWN:
				movey = 0
	x+= movex
	y+= movey

	random = (180,40,180)
	screen.fill(random)
	screen.blit(background, (0, 0))
	screen.blit(mouseC, (x, y))
	pygame.display.update()
	