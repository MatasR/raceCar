import pygame
import config

import RaceCarPoly
import RaceTrack2
import Timer
import functions

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

carState = 0
# 0 - ready
# 1 - just started
# 2 - passed quarter line
# 3 - passed midway
# 4 - passed 3 quarters line
# 5 - finished

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

    # Draw the track and return track borders for off track collision check
    trackBorders = track.draw(screen)

    # Draw track lines
    lines = track.drawLines(screen)# 0 - quarter, 1 - mid, 2 - 3quarters, 3 - start/finish

    # Draw the car
    car.do(screen)

    # Draw car radars
    car.drawRadars(screen, trackBorders)

    # Update timer and draw it
    time = timer.update(carState, screen)

    # Check for line collisions
    if carState == 0: # Car state - ready
        if car.checkForCollision(lines[3]):
            carState += 1  # Car state - just launched
            print('Lets go!')
    if carState == 1: # Car state - just launched
        if car.checkForCollision(lines[0]):
            carState += 1 # Car state - passed quarter line
            print('1st quarter done.')
    if carState == 2: # Car state - passed quarter line
        if car.checkForCollision(lines[1]):
            carState += 1  # Car state - midway
            print('Half way, keep going!')
    if carState == 3: # Car state - midway
        if car.checkForCollision(lines[2]):
            carState += 1 # Car state - passed 3 quarters line
            print('Almost done, dont give up!')
    if carState == 4: # Car state - passed 3 quarters
        if car.checkForCollision(lines[3]):
            carState += 1  # Car state - finished
            print('You finished!')
            print('Your time is:', time, ' Nice job!')
            print('Best time is:', functions.highscore(time))

    # Off Track collision
    if carState > 0:
        # Outer track
        i = 0
        for point in trackBorders[0]:
            line = (trackBorders[0][i], trackBorders[0][(i + 1) % len(trackBorders[0])])
            if car.checkForCollision(line):
                carState = 6 # Car state - crashed
                print('You crashed! :/')
            i += 1
        # Inner track
        i = 0
        for point in trackBorders[1]:
            line = (trackBorders[1][i], trackBorders[1][(i + 1) % len(trackBorders[1])])
            if car.checkForCollision(line):
                carState = 6  # Car state - crashed
                print('You crashed! :/')
            i += 1

    # End game if car state - finished
    if carState > 4:
        run = False

    # Update the screen
    pygame.display.update()

pygame.quit()
