import pygame
from sys import exit

#initialize pygame
pygame.init()
#creation of empty tab and size of the tab
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Card game")
#set frame rate for an even speed across devices 
clock = pygame.time.Clock()              

#creation of surfaces 
    #SIZE AND CONTENT of the surface (content) of a surface/.convert changes format of image 
background_surface = pygame.image.load("images/table.jpg").convert_alpha()
background_surface = pygame.transform.scale(background_surface, (1200, 600))


#"while true" will create an infinite loop, meaning it will execute it indefinitely until the program is interrupted or terminated
    #all operations inside the while loop are constantly updated 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

 #POSITION of the surface (surface)
    screen.blit(background_surface,(0,0))

    pygame.display.update()
    clock.tick(60)