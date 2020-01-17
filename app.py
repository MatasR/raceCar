import pygame
import config

import RaceCarPoly
import RaceTrack2
import Timer

# Initialize game engine library
pygame.init()

# Create main game window
screen = pygame.display.set_mode((config.screenWidth, config.screenHeight))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

# Create the car
car = RaceCarPoly.RaceCar()
# Create the track
track = RaceTrack2.RaceTrack()
# Create the timer
timer = Timer.Timer()

carState = 0  # 0 - ready, 1 - driving, 2 - midway, 3 - finished

# Main game loop
run = True
while run:
    # FPS
    clock.tick(30)

    # Get all pygame events
    for event in pygame.event.get():
        # Quit window
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    # Reset the screen
    screen.fill((0, 255, 0))

    # Draw the track
    track.draw(screen)

    # Draw the car
    carBody = car.do(screen)

    # Update timer and draw it
    timer.update(carState, screen)

    # Check for collisions
    # Finish line collision
    # 1 Start the game

    # If car waiting - check for finishline collision to start the game
    '''if carState == 0:
        if carBody.colliderect(finishLine):
            carState += 1  # Car state running
            print('Lets go!')
    if carState == 1:
        if carBody.colliderect(midLine):
            carState += 1  # Car state midway
            print('Half way, keep going!')
    if carState == 2:
        if carBody.colliderect(finishLine):
            carState += 1
            print('You finished!')'''
    # Off Track collision

    # print(carBody.colliderect(outterRing))

    # Update the screen
    pygame.display.update()

pygame.quit()
