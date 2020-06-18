import pygame
import config
import functions
from math import *

class RaceCar:
    def __init__(self):
        # Main car configs initialized on first call
        self.width = 20 # 30
        self.length = 40 # 50
        self.x = config.screenWidth / 2 - self.length / 2 - 1  # Starting position
        self.y = config.screenHeight - 35 - self.width / 2  # Starting position
        self.color = config.C_PURPLE

        self.currentSpeed = 0
        self.maxSpeed = 7
        self.accSpeed = 0.5
        self.deccSpeed = self.accSpeed * 2
        self.idleSpeed = self.deccSpeed / 4

        self.carDirection = 0
        self.turnSpeed = 5

        # Calculate each point for car body corners on init for nice math in future
        self.bodyPoints = [
            (# p0
                self.x-self.length/2,# x1
                self.y-self.width/2# y1
            ),
            (# p1
                self.x+self.length/2,# x2
                self.y-self.width/2# y2
            ),
            (# p2
                self.x+self.length/2,# x3
                self.y+self.width/2# y3
            ),
            (# p3
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
        elif key[pygame.K_DOWN]:
            self.currentSpeed -= self.deccSpeed
        # If no acc and no decc - engine idle brake
        else:
            self.currentSpeed -= self.idleSpeed
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

        # Update car x,y axis pos with new values
        self.x += x
        self.y += y

    def draw(self, screen):

        # Car body points NOT rotated (we need it for the rotation function)
        notRotatedBodyPoints = [
            (# p0
                self.x-self.length/2,# x1
                self.y-self.width/2# y1
            ),
            (# p1
                self.x+self.length/2,# x2
                self.y-self.width/2# y2
            ),
            (# p2
                self.x+self.length/2,# x3
                self.y+self.width/2# y3
            ),
            (# p3
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

    def drawRadars(self, screen, trackBorders):

        radarsLength = 500

        radars = [
            [# R1
                (# p0
                    (self.bodyPoints[1][0] + self.bodyPoints[2][0]) / 2,
                    (self.bodyPoints[1][1] + self.bodyPoints[2][1]) / 2
                ),
                (# p1
                    (self.bodyPoints[1][0] + self.bodyPoints[2][0]) / 2 + radarsLength,
                    (self.bodyPoints[1][1] + self.bodyPoints[2][1]) / 2
                ),
                0 # distance to collision
            ],
            [# R2
                (# p0
                    self.bodyPoints[1][0],
                    self.bodyPoints[1][1]
                ),
                (# p1
                    self.bodyPoints[1][0] + radarsLength,
                    self.bodyPoints[1][1]
                ),
                0 # distance to collision
            ],
            [# R3
                (# p0
                    self.bodyPoints[2][0],
                    self.bodyPoints[2][1]
                ),
                (# p1
                    self.bodyPoints[2][0] + radarsLength,
                    self.bodyPoints[2][1]
                ),
                0 # distance to collision
            ],
            [# R4
                (# p0
                    self.bodyPoints[1][0],
                    self.bodyPoints[1][1]
                ),
                (# p1
                    self.bodyPoints[1][0] + radarsLength,
                    self.bodyPoints[1][1]
                ),
                0 # distance to collision
            ],
            [# R5
                (# p0
                    self.bodyPoints[2][0],
                    self.bodyPoints[2][1]
                ),
                (# p1
                    self.bodyPoints[2][0] + radarsLength,
                    self.bodyPoints[2][1]
                ),
                0 # distance to collision
            ],
            [# R6
                (# p0
                    self.bodyPoints[1][0],
                    self.bodyPoints[1][1]
                ),
                (# p1
                    self.bodyPoints[1][0] + radarsLength,
                    self.bodyPoints[1][1]
                ),
                0 # distance to collision
            ],
            [# R7
                (# p0
                    self.bodyPoints[2][0],
                    self.bodyPoints[2][1]
                ),
                (# p1
                    self.bodyPoints[2][0] + radarsLength,
                    self.bodyPoints[2][1]
                ),
                0 # distance to collision
            ]
        ]

        # Rotate all second points arround their first points for carDirection angle
        i = 0
        for R in radars:
            radars[i][1] = functions.rotatePoint2D(R[1][0], R[1][1], R[0][0], R[0][1], self.carDirection)
            i += 1

        # Custom additional rotations for some radars
        radars[1][1] = functions.rotatePoint2D(radars[1][1][0], radars[1][1][1], radars[1][0][0], radars[1][0][1], -10)
        radars[2][1] = functions.rotatePoint2D(radars[2][1][0], radars[2][1][1], radars[2][0][0], radars[2][0][1], 10)

        radars[3][1] = functions.rotatePoint2D(radars[3][1][0], radars[3][1][1], radars[3][0][0], radars[3][0][1], -30)
        radars[4][1] = functions.rotatePoint2D(radars[4][1][0], radars[4][1][1], radars[4][0][0], radars[4][0][1], 30)

        radars[5][1] = functions.rotatePoint2D(radars[5][1][0], radars[5][1][1], radars[    5][0][0], radars[5][0][1], -90)
        radars[6][1] = functions.rotatePoint2D(radars[6][1][0], radars[6][1][1], radars[6][0][0], radars[6][0][1], 90)

        # Draw radars
        for R in radars:
            pygame.draw.line(screen, config.C_BLACK, R[0], R[1], 1)

            # Radars intersection with borders
            # get distance to border for 1st radar and draw a circle there
            radar = R # testing with just one radar
            #trackBorders = trackBorders[1] # testing with just inner track borders
            closestCollision = False  # by default there is no closest collision
            for borders in trackBorders:
                i = 0 # index for trackPoints
                for trackPoint in borders:
                    # define track line from trackPoints
                    trackLine = (borders[i], borders[(i+1) % len(borders)])
                    # check if our radar is colliding with current trackLine
                    collision = functions.collisionDetection(radar, trackLine)
                    if collision:
                        # get distance from 1st radar point (car body) till collision
                        newDistance = functions.distance(radar[0], collision)
                        # check if it is closer than older collisions
                        if radar[2] == 0 or newDistance < radar[2]:
                            # assign new closest collision distance
                            radar[2] = newDistance
                            # and position
                            closestCollision = collision
                    i += 1

            # if there was any collision
            if closestCollision:
                # then draw the circle in closest collision position
                pygame.draw.circle(screen, config.C_BLACK, (int(closestCollision[0]), int(closestCollision[1])), 4)
        '''for trackPoints in trackBorders: # 2 iterations for outer track and inner track
            i = 0
            for borderPoint in trackPoints:
                collision = functions.collisionDetection((trackPoints[i], trackPoints[(i+1) % len(trackPoints)]), radar)
                if collision:
                    distance = functions.distance(radar[0], collision)
                    if distance < radars[0][2] or radars[0][2] == 0:
                        closestCollision = collision
                        radars[0][2] = distance
                    pygame.draw.circle(screen, config.C_BLACK, (int(closestCollision[0]), int(closestCollision[1])), 5)

                    # I only need to draw circle for nearest collision
                i += 1'''

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