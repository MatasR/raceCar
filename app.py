import pygame
from math import *

import config

import RaceTrack

pygame.init()

screen = pygame.display.set_mode((config.screenWidth, config.screenHeight))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()


class RaceCar:
    def __init__(self):
        # Main car configs initialized on first call
        self.width = 30
        self.length = 50
        self.x = config.screenWidth / 2 - self.length - 3  # Starting position
        self.y = config.screenHeight - 50 - self.width / 2  # Starting position
        self.color = (255, 0, 0)

        self.currentSpeed = 0
        self.maxSpeed = 7
        self.accSpeed = 0.5

        self.carDirection = 0
        self.carRotationSpeed = 2.5
        self.tiresDirection = 0
        self.turnSpeed = 5
        self.maxTurnAngle = 45

    def keys(self):
        # Change the parameters of the car according to pushed key
        key = pygame.key.get_pressed()

        # Accelerate
        if key[pygame.K_UP]:
            if self.currentSpeed < self.maxSpeed:
                self.currentSpeed += self.accSpeed
        # Deccelerate
        if key[pygame.K_DOWN]:
            self.currentSpeed -= self.accSpeed
        # Turn
        if key[pygame.K_LEFT]:
            self.rotateTires("LEFT")
        elif key[pygame.K_RIGHT]:
            self.rotateTires("RIGHT")
        else:
            self.rotateTires("CENTER")

    def rotateTires(self, direction):
        if direction == "LEFT":
            if self.tiresDirection > -self.maxTurnAngle:
                self.tiresDirection -= self.turnSpeed
        if direction == "RIGHT":
            if self.tiresDirection < self.maxTurnAngle:
                self.tiresDirection += self.turnSpeed
        if direction == "CENTER":
            if self.tiresDirection > 0:
                self.tiresDirection -= self.turnSpeed / 2
            elif self.tiresDirection < 0:
                self.tiresDirection += self.turnSpeed / 2

    def rotate(self, direction):
        if direction == "LEFT":
            self.carDirection -= self.turnSpeed
        if direction == "RIGHT":
            self.carDirection += self.turnSpeed

        # Convert direction in (-)180 angle
        if self.carDirection > 180:
            self.carDirection -= 360
        if self.carDirection < -180:
            self.carDirection += 360

    def move(self):
        # Change car position according to (updated) parameters

        # Car cant move backwards - stop it instead
        if self.currentSpeed < 0:
            self.currentSpeed = 0

        # Calculate new car position by its speed and tires direction
        x = cos(radians(self.carDirection)) * self.currentSpeed
        y = sin(radians(self.carDirection)) * self.currentSpeed

        # If car is moving, slowly align its direction with tires direction
        if self.currentSpeed > 0:
            if self.tiresDirection > 0:
                self.carDirection += self.carRotationSpeed
                self.tiresDirection -= self.carRotationSpeed
            if self.tiresDirection < 0:
                self.carDirection -= self.carRotationSpeed
                self.tiresDirection += self.carRotationSpeed

        if self.carDirection > 180:
            self.carDirection -= 360
        if self.carDirection <= -180:
            self.carDirection += 360

        # Update car x,y axis pos
        self.x += x
        self.y += y

    def drawTires(self, carBody):
        # Draw tires Surface
        carTires = pygame.Surface((self.length / 2, self.width))
        carTires.set_colorkey((0, 0, 0))  # No idea what it does but its necessary
        # Draw actual tires rect
        pygame.draw.polygon(carTires, (0, 0, 255), [
            [0, 0],
            [self.length / 2, self.width / 2],
            [0, self.width]
        ])
        # Car Tires math for rotation function
        notYetRotatedCarTiresRect = carTires.get_rect()
        carTiresCenter = (
            notYetRotatedCarTiresRect.center[0] + self.length / 2,
            notYetRotatedCarTiresRect.center[1]
        )
        carTiresRotated = pygame.transform.rotate(carTires, -self.tiresDirection)
        rotatedRect = carTiresRotated.get_rect()
        rotatedRect.center = carTiresCenter

        # Put rotated tires onto rotated car body
        carBody.blit(carTiresRotated, rotatedRect)

    def draw(self):
        # Draw updated car position (x,y) into the screen
        carBody = pygame.Surface((self.length, self.width))
        carBody.fill(self.color)
        carBody.set_colorkey((0, 0, 0))  # No idea what it does but its necessary

        # Draw rotated tires onto non rotated car body
        self.drawTires(carBody)

        # Invisible rotation stuff
        # Make rectangle out of not-yet-rotated surface (for future math stuff)
        notYetRotatedRect = carBody.get_rect()
        # Store its center (for future alignment) adding car x,y position
        carBodyCenter = (
            notYetRotatedRect.center[0] + self.x,
            notYetRotatedRect.center[1] + self.y
        )

        # Rotate carBody surface
        carBodyRotated = pygame.transform.rotate(carBody, -self.carDirection)
        # Create new rectangle out of the rotated carBody surface
        rotatedRect = carBodyRotated.get_rect()
        # Put new rectangle in the old rectangle (not yet rotated) center
        rotatedRect.center = carBodyCenter

        # Update screen
        screen.blit(carBodyRotated, rotatedRect)

        return rotatedRect

    def do(self):
        # Container for all necessary functions
        self.keys()
        self.move()
        carRect = self.draw()

        # Return two front coords
        return carRect


class Timer:
    def __init__(self):
        self.x = config.screenWidth / 2
        self.y = config.screenHeight / 2
        self.time = 0

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("%s" % float(self.time), True, config.C_WHITE)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        screen.blit(text, textRect)

    def update(self, carState):
        if carState > 0 and carState < 3:
            self.time += 0.5
        self.draw()


# Create the car
car = RaceCar()
# Create the track
track = RaceTrack.RaceTrack()
# Create the timer
timer = Timer()

carState = 0  # 0 - ready, 1 - driving, 2 - midway, 3 - finished

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
    innerRing, outterRing, finishLine, midLine = track.draw(screen)

    # Draw the car
    carBody = car.do()

    # Update timer and draw it
    timer.update(carState)

    # Check for collisions
    # Finish line collision
    # 1 Start the game

    # If car waiting - check for finishline collision to start the game
    if carState == 0:
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
            print('You finished!')
    # Off Track collision

    # print(carBody.colliderect(outterRing))

    # Update the screen
    pygame.display.update()

pygame.quit()
