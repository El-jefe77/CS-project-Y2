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
    #this variable can change the size and fill (content) of a surface
background_surface = pygame.image.load("images/table.jpg")

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
    #test update repo
    clock.tick(60)