import pygame
import config

class Timer:
    def __init__(self):
        self.x = config.screenWidth / 2
        self.y = config.screenHeight / 2
        self.time = 0

    def draw(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("%s" % float(self.time), True, config.C_WHITE)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        screen.blit(text, textRect)

    def update(self, carState, screen):
        if carState > 0 and carState < 5:
            self.time += 0.5
        self.draw(screen)

        return self.time