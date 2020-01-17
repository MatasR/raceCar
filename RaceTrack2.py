import pygame
import config

class RaceTrack:
    def draw(self, screen):

        # Track outer points
        outerPoints = [
            (config.screenWidth / 2, config.screenHeight),
            (config.screenWidth - 10, 200),
            (config.screenWidth - 10, 100),
            (config.screenWidth - 100, 10),
            (config.screenWidth / 2 + 200, 10),
            (config.screenWidth / 2, 200),
            (config.screenWidth / 2 - 200, 10),
            (100, 10),
            (10, 100),
            (10, 100),
            (10, 200),
            (10, 200),
            (config.screenWidth / 2, config.screenHeight)
        ]

        # Track inner points
        innerPoints = [
            (config.screenWidth / 2, config.screenHeight - 100),
            (config.screenWidth - 110, 175),
            (config.screenWidth - 110, 110),
            (config.screenWidth / 2 + 250, 110),
            (config.screenWidth / 2, 300),
            (config.screenWidth / 2 - 250, 110),
            (110, 110),
            (110, 175),
            (110, 175),
            (config.screenWidth / 2, config.screenHeight - 100)
        ]

        # Track fill outer
        pygame.draw.polygon(screen, config.C_GRAY, outerPoints)

        # Track fill inner
        pygame.draw.polygon(screen, config.C_GREEN, innerPoints)

        # OUTER HEART
        # Right side of the heart
        i = 0
        for x in outerPoints:
            pygame.draw.line(screen, config.C_YELLOW, outerPoints[i], outerPoints[i+1], 3)
            i += 1
            # If last point - break the loop.
            if i+1 == len(outerPoints):
                break
        '''pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth/2, config.screenHeight), (config.screenWidth - 10, 200), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth - 10, 200), (config.screenWidth - 10, 100), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth - 10, 100), (config.screenWidth - 100, 10), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth - 100, 10), (config.screenWidth / 2 + 200, 10), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth / 2 + 200, 10), (config.screenWidth / 2, 200), 3)'''

        # Left side of the heart
        i = 0
        for x in innerPoints:
            pygame.draw.line(screen, config.C_YELLOW, innerPoints[i], innerPoints[i + 1], 3)
            i += 1
            # If last point - break the loop.
            if i + 1 == len(innerPoints):
                break
        '''pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth / 2, 200), (config.screenWidth / 2 - 200, 10), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth / 2 - 200, 10), (100, 10), 3)
        pygame.draw.line(screen, config.C_YELLOW, (100, 10), (10, 100), 3)
        pygame.draw.line(screen, config.C_YELLOW, (10, 100), (10, 200), 3)
        pygame.draw.line(screen, config.C_YELLOW, (10, 200), (config.screenWidth/2, config.screenHeight), 3)'''

        # INNER HEART
        # Right side of the heart
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth / 2, config.screenHeight - 100), (config.screenWidth - 110, 175), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth - 110, 175), (config.screenWidth - 110, 110), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth - 110, 110), (config.screenWidth / 2 + 250, 110), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth / 2 + 250, 110), (config.screenWidth / 2, 300), 3)

        # Left side of the heart
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth / 2, 300), (config.screenWidth / 2 - 250, 110), 3)
        pygame.draw.line(screen, config.C_YELLOW, (config.screenWidth / 2 - 250, 110), (110, 110), 3)
        pygame.draw.line(screen, config.C_YELLOW, (110, 110), (110, 175), 3)
        pygame.draw.line(screen, config.C_YELLOW, (110, 175), (config.screenWidth / 2, config.screenHeight - 100), 3)