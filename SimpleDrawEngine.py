import pygame
from pygame.locals import *

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
	def __init__(self, size, antialias, color, vector2, screen):
		self.size = size
		self.antialias = antialias
		self.color = color
		self.vector2 = vector2
		self.screen = screen
		
	def draw(self, text, position):
		self.font = pygame.font.Font(pygame.font.get_default_font(), self.size)
		self.text = self.font.render(text, self.antialias, self.color)

		# makes the text be centered
		self.screen.blit(self.text, (position[0] - self.text.get_rect().width / 2, position[1]))
