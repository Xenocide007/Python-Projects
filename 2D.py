mouseCO = "Mario.png"
running = True
import os
import random
import pygame, sys
from pygame.locals import *

pygame.init()

#screen = pygame.display.set_mode((1500, 800))
screen = pygame.display.set_mode((750, 400))
mouseC = pygame.image.load(mouseCO).convert_alpha()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.display.set_caption("Stuff")

lead_x = 400
lead_y = 300
lead_x_change = 0
lead_y_change = 0

random = (180,40,180)
clock = pygame.time.Clock()
gameExit = False

while not gameExit:
	for event in pygame.event.get():
		print("event.type", event.type)
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -5
				lead_y_change = 0
			if event.key == pygame.K_RIGHT:
				lead_x_change = 5
				lead_y_change = 0
			if event.key == pygame.K_UP:
				lead_y_change = -5
				lead_x_change = 0
			if event.key == pygame.K_DOWN:
				lead_y_change = 5
				lead_x_change = 0
	else:
		print("this is dangerous")
		lead_x_change = lead_y_change = 0
	if lead_x > 1360:
		lead_x_change = -5
	if lead_x < 0:
		lead_x_change = 5
	if lead_y > 650:
		lead_y_change = -5
	if lead_y < 0:
		lead_y_change = 5		


	lead_x += lead_x_change
	lead_y += lead_y_change
	screen.fill(random)
	screen.blit(screen, (0, 0))
	screen.blit(mouseC, (lead_x, lead_y))

	pygame.display.update()

	clock.tick(100)

pygame.quit()
quit()

