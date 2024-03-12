import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up display
pygame.display.set_caption("Card game")
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169, 169, 169)

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48)

# Load image
background_surface = pygame.image.load("images/menu.jpg").convert_alpha()
background_surface = pygame.transform.scale(background_surface, (1200, 700))

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# Main menu loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                # Run main.py when "Play" is pressed
                subprocess.run(["python", "main.py"])
            elif quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            elif settings_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("HOLA SETTINGS :)")

    # Draw background image
    screen.blit(background_surface, (0, 0))

    # Draw title
    draw_text("POKER", title_font, black, screen.get_width() // 2, screen.get_height() // 4)

    # Draw play button
    play_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 - 25, 200, 50)
    pygame.draw.rect(screen, gray, play_button)
    draw_text("PLAY", font, black, screen.get_width() // 2, screen.get_height() // 2)

    # Draw quit button
    quit_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50, 200, 50)
    pygame.draw.rect(screen, gray, quit_button)
    draw_text("QUIT", font, black, screen.get_width() // 2, screen.get_height() // 2 + 75)
    quit_button_rect = quit_button

    # Draw settings button
    settings_button = pygame.Rect(screen.get_width() - 120, 20, 300, 40)
    pygame.draw.rect(screen, gray, settings_button)
    draw_text("SETTINGS", font, black, screen.get_width() -60 , 40)
    settings_button_rect = settings_button

    # Define play_button_rect
    play_button_rect = play_button

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)