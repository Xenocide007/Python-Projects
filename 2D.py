import sys  
import pygame  

from pygame.locals import *  

#Initalize the Program  
pygame.init()  
#Create the Screen  
w =  640         
h = 480 
screen= pygame.display.set_mode((w,h), 0, 32)  
pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 480))  
pygame.draw.rect(screen, (0, 255, 0), (640, 0,540, 480))  

pygame.display.flip()

fname = "mario.png" 
player = pygame.image.load (fname).convert()
screen.blit (player, (100, 100))
pygame.display.update()   

y = 300 
x = 100 
y_dir = 0 
x_dir = 0 

while True:  
    for event in pygame.event.get():   
        if event.type == QUIT:  
            pygame.quit()  
            sys.exit()

        if event.type == KEYDOWN:  
            if event.key == K_UP:   
                y_dir = -1  
            if event.key == K_DOWN:   
                y_dir = 1 
            if event.key == K_RIGHT:  
                x_dir = 1 
            if event.key == K_LEFT:  
                x_dir = -1 


        if event.type == KEYUP:  
            if event.key == K_UP or event.key == K_DOWN:   
                y_dir = 0 
            if event.key == K_LEFT or event.key == K_RIGHT:  
                x_dir = 0 
    
    y += y_dir  
    x += x_dir   
    
    screen.fill ((0, 0, 0))   
    screen.blit (player, (x, y))  
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 480))
    pygame.draw.rect(screen, (0, 255, 0), (640, 0,540, 480))

    pygame.display.update() 
