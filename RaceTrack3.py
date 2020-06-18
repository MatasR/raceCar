import pygame
import config

class RaceTrack:
    def __init__(self):
        # Track outer points
        self.outerPoints = [
            (10, 10),
            (config.screenWidth - 10, 10),
            (config.screenWidth - 10, config.screenHeight - 10),
            (10, config.screenHeight - 10)
        ]

        # Track inner points
        self.innerPoints = [
            (100, 100),
            (config.screenWidth - 100, 100),
            (config.screenWidth - 100, config.screenHeight - 100),
            (100, config.screenHeight - 100)
        ]

    def draw(self, screen):

        # Track fill outer
        pygame.draw.polygon(screen, config.C_GRAY, self.outerPoints)

        # Track fill inner
        pygame.draw.polygon(screen, config.C_GREEN, self.innerPoints)

        # OUTER HEART (lines)
        i = 0
        for x in self.outerPoints:
            pygame.draw.line(screen, config.C_YELLOW, self.outerPoints[i], self.outerPoints[(i + 1) % len(self.outerPoints)], 3)
            i += 1

        # INNER HEART (lines)
        i = 0
        for x in self.innerPoints:
            pygame.draw.line(screen, config.C_YELLOW, self.innerPoints[i], self.innerPoints[(i + 1) % len(self.innerPoints)], 3)
            i += 1

        return (self.outerPoints, self.innerPoints)

    def drawLines(self, screen):

        # Quarter line
        pygame.draw.line(screen, config.C_BLUE, self.outerPoints[2], self.innerPoints[2], 1)
        quarterLine = (self.outerPoints[2], self.innerPoints[2])

        # Mid line
        midLine = (self.outerPoints[1], self.innerPoints[1])
        pygame.draw.line(screen, config.C_BLUE, midLine[0], midLine[1], 1)

        # Three Quarters line
        threeQuartersLine = (self.outerPoints[0], self.innerPoints[0])
        pygame.draw.line(screen, config.C_BLUE, threeQuartersLine[0], threeQuartersLine[1], 1)

        # Start/finish line
        #finishLine = (self.outerPoints[0], self.innerPoints[0])
        finishLine = (
            (config.screenWidth / 2, config.screenHeight - 100),
            (config.screenWidth / 2, config.screenHeight)
        )
        pygame.draw.line(screen, config.C_YELLOW, finishLine[0], finishLine[1], 1)

        return quarterLine, midLine, threeQuartersLine, finishLine