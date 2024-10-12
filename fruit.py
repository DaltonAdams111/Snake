import pygame
import random
from constants import *

class Fruit:
	def __init__(self, x_position, y_position, width, height):
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x_position, y_position, width, height)

	def draw(self, surface):
		pygame.draw.rect(surface, "red", self.rect)

	def move(self, snake):
		while True:
			self.rect.left = random.randrange(0, pygame.display.Info().current_w - self.width, self.width)
			self.rect.top = random.randrange(0, pygame.display.Info().current_h - self.height, self.height)

			if self.rect.collidelist(snake) == -1:
				break