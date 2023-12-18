import pygame
from sys import exit

#initialize pygame
pygame.init()
#creation of empty tab and size of the tab
pygame.display.set_caption("Card game")
screen = pygame.display.set_mode((1200,600))
#set frame rate for an even speed across devices 
clock = pygame.time.Clock()              

#creation of surfaces 
    #Surface content (background)
background_surface = pygame.image.load("images/table.jpg")
    #adjust size of surface
background_surface = pygame.transform.scale(background_surface, (1200, 600))





#"while true" will create an infinite loop, meaning it will execute it indefinitely until the program is interrupted or terminated
    #all operations inside the while loop are constantly updated 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

 #this surface determines position of the shape (surface)
    screen.blit(background_surface,(0,0))

    pygame.display.update()
    clock.tick(60)