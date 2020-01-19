import pygame
import config
import functions
from math import *

class RaceCar:
    def __init__(self):
        # Main car configs initialized on first call
        self.width = 30 # 30
        self.length = 50 # 50
        self.x = config.screenWidth / 2 - self.length / 2 - 1  # Starting position
        self.y = config.screenHeight - 35 - self.width / 2  # Starting position
        self.color = config.C_PURPLE

        self.currentSpeed = 0
        self.maxSpeed = 7
        self.accSpeed = 0.5

        self.carDirection = 0
        self.turnSpeed = 5

        # Calculate each point for car body corners on init for nice math in future
        self.bodyPoints = [
            (# p1
                self.x-self.length/2,# x1
                self.y-self.width/2# y1
            ),
            (# p2
                self.x+self.length/2,# x2
                self.y-self.width/2# y2
            ),
            (# p3
                self.x+self.length/2,# x3
                self.y+self.width/2# y3
            ),
            (# p4
                self.x-self.length/2,# x4
                self.y+self.width/2# y4
            )
        ]

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
            self.rotate("LEFT")
        elif key[pygame.K_RIGHT]:
            self.rotate("RIGHT")

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

        # Calculate new car center position by its speed and direction
        x = cos(radians(self.carDirection)) * self.currentSpeed
        y = sin(radians(self.carDirection)) * self.currentSpeed

        '''if self.carDirection > 180:
            self.carDirection -= 360
        if self.carDirection <= -180:
            self.carDirection += 360'''

        # Update car x,y axis pos with new values
        self.x += x
        self.y += y

        #print(self.carDirection)

    def draw(self, screen):

        # Car body points NOT rotated (we need it for the rotation function)
        notRotatedBodyPoints = [
            (# p1
                self.x-self.length/2,# x1
                self.y-self.width/2# y1
            ),
            (# p2
                self.x+self.length/2,# x2
                self.y-self.width/2# y2
            ),
            (# p3
                self.x+self.length/2,# x3
                self.y+self.width/2# y3
            ),
            (# p4
                self.x-self.length/2,# x4
                self.y+self.width/2# y4
            )
        ]

        # we should use relative x, y coords instead of global
        # because we will rotate around car body center, not around screen bottom left corner
        # this is done in functions file

        # Calculate new car body points position with angle to rotate after
        # And get rotated body points
        i = 0
        for point in notRotatedBodyPoints:
            self.bodyPoints[i] = functions.rotatePoint2D(point[0], point[1], self.x, self.y, self.carDirection)
            i += 1

        # Draw rotated car body
        pygame.draw.polygon(screen, self.color, self.bodyPoints)

    def do(self, screen):
        # Container for all necessary functions
        self.keys()
        self.move()
        self.draw(screen)

    def checkForCollision(self, line):

        # take all 4 car body lines, and check with given line
        i = 0
        for point in self.bodyPoints:
            bodyLine = (self.bodyPoints[i], self.bodyPoints[(i+1) % len(self.bodyPoints)])
            if functions.collisionDetection(bodyLine, line):
                return True
            i += 1

        return False