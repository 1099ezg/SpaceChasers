import pygame
import random
import sys
from pygame.locals import *
import pygame.mixer

# Pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# Load images
main_player = pygame.image.load('spacechaser\\spaceship.png')
main_player = pygame.transform.scale(main_player, (60, 60))  # Scale the spaceship image
background = pygame.image.load('spacechaser\\space_background.png')
asteroid_image = pygame.image.load('spacechaser\\asteroid_image.png')
asteroid_image = pygame.transform.scale(asteroid_image, (90, 90))
title = pygame.image.load('spacechaser\\spacechasers_title.png')
title_menu_background = pygame.image.load('spacechaser\\Menu_background.png')
title_menu_background = pygame.transform.scale(title_menu_background, (screen_width, screen_height))
title_menu_surface = pygame.Surface((screen_width, screen_height))

# Music Set Up Section

# load music:
pygame.mixer.init()
pygame.mixer.music.load('spacechaser\\spacechaser_music.mp3') 
# Begin playing music at start of game loop
pygame.mixer.music.play(-1)

# Menu Section:
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
# Text font:
font = pygame.font.Font(None, 36)  # Common font for text
# Display caption
pygame.display.set_caption("Space Chaser")

# Set up variables for main menu and game started or over
show_main_menu = True
game_started = False
# Tracking variable to see if game is over
game_over = False

# Set up variables for scoring
score = 0
high_score = 0

# Time variable for difficulty speed increase
elapsed_time = 0
#increase message
speeding_up_timer = 0
show_speeding_up_message = False

# Spaceship section

spaceship_width = 40 # Width of spaceship
spaceship_height = 40 # Height of spaceship
spaceship_x = 100 # Ensure spaceship starts at left of the screen

# Ensure spaceship starts at center of the screen
spaceship_y = screen_height // 2 - spaceship_height // 2 
# Setup Speed for spaceship (Should not move except up and down)
spaceship_speed = 0 

# Asteroid Section

# Define variables for asteroid spawning
asteroids = [] # List of asteroids
asteroid_speed = 5 # Speed of asteroid
asteroid_spawn_timer = 0 # Timer for asteroid spawning
asteroid_width = 40 # Width of asteroid
asteroid_height = 40 # Height of asteroid
max_asteroids = int(screen_width / (asteroid_width * 1.5))  # Maximum asteroids based on screen width and asteroid size


# Main game loop
while running:

    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Blit the title menu background onto the screen
    screen.blit(title_menu_background, (0, 0))

    for event in pygame.event.get(): # Check for events
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button trigger
            if show_main_menu:
                if not game_started:
                    show_main_menu = False
                    game_started = True
                    score = 0
                    spaceship_y = screen_height // 2 - spaceship_height // 2
                    asteroids.clear()
                else:
                    # Handle game logic here
                    pass

    keys = pygame.key.get_pressed()

    # Draw the screen
    screen.fill((0, 0, 0))
    if show_main_menu:
        screen.blit(title_menu_background, (0, 0))
        screen.blit(title, (100, 100))

        # Calculate the center point of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2
        pygame.draw.rect(screen, WHITE, ((screen_width - 200) // 2, 415 - 25, 200, 50))

        
        # display high score
        high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
        high_score_rect = high_score_text.get_rect(center=(center_x, center_y - 50))  # Move up from the center
        screen.blit(high_score_text, high_score_rect)
    
        # start game button
        start_game_text = font.render("Start Game", True, BLACK)
        start_game_rect = start_game_text.get_rect(center=(center_x, center_y + 50))  # Move down from the center
        pygame.draw.rect(screen, WHITE, start_game_rect)  # Draw background for the button
        screen.blit(start_game_text, start_game_rect)
        
    else:
        screen.blit(background, (0, 0))
        screen.blit(main_player, (spaceship_x, spaceship_y))
        for asteroid_rect in asteroids:
            screen.blit(asteroid_image, (asteroid_rect.x, asteroid_rect.y))

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    if game_started:
        if keys[pygame.K_UP]:
            spaceship_y -= 5  # moving up
        if keys[pygame.K_DOWN]:
            spaceship_y += 5 # move down
        
        # Apply boundaries for the spaceship
        spaceship_y = max(0, min(spaceship_y, screen_height - spaceship_height))

        # Increase difficulty over time
        elapsed_time += clock.get_time()
        if elapsed_time >= 20000:  # 20 seconds
            asteroid_speed += 2  # Increase the asteroid speed
            elapsed_time = 0  # Reset the timer

            # add in a speeding up message for each diff increase
            show_speeding_up_message = True
            speeding_up_timer = pygame.time.get_ticks()

        # show speeding up message for 2 seconds
        current_time = pygame.time.get_ticks()
        if show_speeding_up_message and current_time - speeding_up_timer >= 3000:  # 3000 milliseconds = 3 seconds
            show_speeding_up_message = False

        #spawn astroids based on speed
        asteroid_spawn_interval = max(20, int(max_asteroids / asteroid_speed))  # Minimum of 20 frames between spawns

        # Update asteroid positions
        for asteroid_rect in asteroids:
            asteroid_rect.x -= asteroid_speed  # Move asteroids towards the spaceship

        # collision fix
        spaceship_collision_rect = pygame.Rect(spaceship_x + 5, spaceship_y + 5, spaceship_width - 10, spaceship_height - 10)

        # Spawn new asteroids timer
        if len(asteroids) < max_asteroids:
            asteroid_spawn_timer += 1
            if asteroid_spawn_timer >= asteroid_spawn_interval:
                asteroid_spawn_timer = 0
                asteroid_height = random.randint(20, 50)  # Adjusted asteroid size
                asteroid_width = asteroid_height  # Keep it same size as height
                asteroid_x = screen_width
                asteroid_y = random.randint(0, screen_height - asteroid_height)
                asteroid_rect = pygame.Rect(asteroid_x, asteroid_y, asteroid_width, asteroid_height)
                asteroids.append(asteroid_rect)


# Collision detection
            for asteroid_rect in asteroids:
                asteroid_collision_rect = pygame.Rect(asteroid_rect.x, asteroid_rect.y, asteroid_width, asteroid_height)
                if spaceship_collision_rect.colliderect(asteroid_collision_rect):
                    if score > high_score:
                        high_score = score
                    game_over = True  
                    game_started = False  # Game has ended
                    spaceship_velocity = 0
                    spaceship_y = screen_height // 2 - spaceship_height // 2  # Reset spaceship position
                    asteroids.clear()  # Clear asteroids list
                    asteroid_speed = 5  # Reset asteroid speed
                    break  # Exit the loop since the game has ended
                elif asteroid_rect.x + asteroid_width <= 0:
                    asteroids.remove(asteroid_rect)

# game over block
    if game_over:
    # Clear the screen
        screen.blit(background, (0, 0))

        # Display "Game Over" message
        game_over_text = font.render(f"Game Over! Your score was: {score}", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, game_over_rect)

        # Draw "Back To Menu" button
        back_to_menu_text = font.render("Back To Menu", True, BLACK)
        back_to_menu_rect = back_to_menu_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        pygame.draw.rect(screen, WHITE, back_to_menu_rect)  # Draw background for the button
        screen.blit(back_to_menu_text, back_to_menu_rect)

        pygame.display.flip()

        # Check for the "Back To Menu" button click
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_to_menu_rect.collidepoint(event.pos):
                    game_over = False
                    show_main_menu = True
                    game_started = False
                    spaceship_y = screen_height // 2 - spaceship_height // 2
                    asteroids.clear()
                    asteroid_speed = 5
                    score = 0  # Reset the score
        continue

    # display speeding up message 
    if show_speeding_up_message:
            speeding_up_text = font.render("Speeding Up!", True, WHITE)
            screen.blit(speeding_up_text, (screen_width // 2 - speeding_up_text.get_width() // 2, 20))

    # Update score
    score += 1

    pygame.display.flip()
    clock.tick(60)  # 60 FPS
    screen.blit(title_menu_surface, (0, 0))
    # stop music 
    if not running:
        pygame.mixer.music.stop()

pygame.quit()