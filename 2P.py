mouseCO = "Mario.png"
running = True
import os
import random
import pygame, sys
from pygame.locals import *

pygame.init()

#screen = pygame.display.set_mode((1500, 800))
screen = pygame.display.set_mode((800, 600))
mouseC = pygame.image.load(mouseCO).convert_alpha()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.display.set_caption("Mario")

x = 300
y = 300
movex = 0
movey = 0

random = (0,200,255)
clock = pygame.time.Clock()
gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				movex = -5
			elif event.key == K_RIGHT:
				movex = +5
			elif event.key == K_UP:
				movey = -10
			elif event.key == K_DOWN:
				movey = +5
		if event.type == KEYUP:
			if event.key == K_LEFT:
				movex = 0
			elif event.key == K_RIGHT:
				movex = 0
			elif event.key == K_UP:
				movey = 10, 
				movey = 0
			elif event.key == K_DOWN:
				movey = 0
			elif event.key == K_ESCAPE:
				terminate()

	if x > 670:
		movex = 0
	if x < 0:
		movex = 0
	if y > 460:
		movey = 0
	if y < 0:
		movey = 0

	x += movex
	y += movey
	screen.fill(random)
	screen.blit(screen, (0, 0))
	screen.blit(mouseC, (x, y))

	pygame.display.update()

	clock.tick(100)

pygame.quit()
quit()
