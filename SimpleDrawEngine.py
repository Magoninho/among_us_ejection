import pygame


class Circle:
    def __init__(self, screen, color, center, radius):
        self.screen = screen
        self.color = color
        self.center = center
        self.radius = radius
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)


class Rect:
    def __init__(self, screen, color, rect):
        self.screen = screen
        self.color = color
        self.rect = rect
        pygame.draw.rect(self.screen, self.color, self.rect)

class Line:
    def __init__(self, screen, color, start , end, thiccness):
        self.screen = screen
        self.color = color
        self.start = start
        self.end = end
        self.thiccness = thiccness
        pygame.draw.line(self.screen, self.color, self.start, self.end, self.thiccness)

class Text:
    def write_text(font, size, text, antialias, color, vector2, screen):
        pygame.font.init()
        font = pygame.font.SysFont(font, size)
        text = font.render(text, antialias, color)
        screen.blit(text, vector2)
