import pygame
import config

class RaceTrack:
    def draw(self, screen):
        # Outter ring
        outterRing = pygame.draw.circle(screen, config.C_GRAY,
                                        ((int)(config.screenWidth / 2), (int)(config.screenHeight / 2)), 250)
        # Inner ring
        innerRing = pygame.draw.circle(screen, config.C_GREEN,
                                       ((int)(config.screenWidth / 2), (int)(config.screenHeight / 2)), 150)
        # Start/finish line
        finishLine = pygame.draw.line(screen, config.C_YELLOW, ((int)(config.screenWidth / 2), config.screenHeight),
                                      ((int)(config.screenWidth / 2), (int)(config.screenHeight - 100)), 5)
        # Mid line
        midLine = pygame.draw.line(screen, config.C_BLUE, ((int)(config.screenWidth / 2), 0),
                                   ((int)(config.screenWidth / 2), 100), 5)

        return innerRing, outterRing, finishLine, midLine
