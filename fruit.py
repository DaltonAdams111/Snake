import pygame
import random
from constants import *

class Fruit:
	def __init__(self, x_position, y_position, width, height):
		self.width = int(width)
		self.height = int(height)
		self.rect = pygame.Rect(int(x_position), int(y_position), self.width, self.height)

	def draw(self, surface):
		pygame.draw.rect(surface, "red", self.rect)

	def move(self, snake):
		if len(snake) >= (SCREEN_WIDTH / self.width) * (SCREEN_HEIGHT / self.height):
			return
		
		while True:
			self.rect.left = random.randrange(0, SCREEN_WIDTH - self.width, self.width)
			self.rect.top = random.randrange(0, SCREEN_HEIGHT - self.height, self.height)

			if self.rect.collidelist(snake) == -1:
				break