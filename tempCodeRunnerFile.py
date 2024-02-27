import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Card Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169, 169, 169)

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48)

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
                # Run the main game script
                subprocess.run(["python", "main.py"])

            elif quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            elif settings_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Settings button pressed")

    # Clear the screen
    screen.fill(white)

    # Draw title
    draw_text("POKER", title_font, black, width // 2, height // 4)

    # Draw play button
    play_button = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
    pygame.draw.rect(screen, gray, play_button)
    draw_text("PLAY", font, black, width // 2, height // 2)
    play_button_rect = play_button

    # Draw quit button
    quit_button = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50)
    pygame.draw.rect(screen, gray, quit_button)
    draw_text("QUIT", font, black, width // 2, height // 2 + 75)
    quit_button_rect = quit_button

    # Draw settings button
    settings_button = pygame.Rect(width - 120, 20, 100, 40)
    pygame.draw.rect(screen, gray, settings_button)
    draw_text("SETTINGS", font, black, width - 70, 40)
    settings_button_rect = settings_button

    #frame rate
    pygame.display.flip()
    pygame.time.Clock().tick(60)
