import pygame
import config

class RaceTrack:
    def __init__(self):
        # Track outer points
        self.outerPoints = [
            (config.screenWidth / 2, config.screenHeight),
            (config.screenWidth - 10, 200),
            (config.screenWidth - 10, 100),
            (config.screenWidth - 100, 10),
            (config.screenWidth / 2 + 200, 10),
            (config.screenWidth / 2, 200),
            (config.screenWidth / 2 - 200, 10),
            (100, 10),
            (10, 100),
            (10, 200),
        ]

        # Track inner points
        self.innerPoints = [
            (config.screenWidth / 2, config.screenHeight - 100),
            (config.screenWidth - 110, 175),
            (config.screenWidth - 110, 110),
            (config.screenWidth / 2 + 250, 110),
            (config.screenWidth / 2, 300),
            (config.screenWidth / 2 - 250, 110),
            (110, 110),
            (110, 175),
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
        pygame.draw.line(screen, config.C_BLUE, self.outerPoints[1], self.innerPoints[1], 1)
        quarterLine = (self.outerPoints[1], self.innerPoints[1])
        # Mid line
        pygame.draw.line(screen, config.C_BLUE, self.outerPoints[5], self.innerPoints[4], 1)
        midLine = (self.outerPoints[5], self.innerPoints[4])
        # Three Quarters line
        pygame.draw.line(screen, config.C_BLUE, self.outerPoints[9], self.innerPoints[7], 1)
        threeQuartersLine = (self.outerPoints[9], self.innerPoints[7])
        # Start/finish line
        pygame.draw.line(screen, config.C_YELLOW, self.outerPoints[0], self.innerPoints[0], 1)
        finishLine = (self.outerPoints[0], self.innerPoints[0])

        return quarterLine, midLine, threeQuartersLine, finishLine