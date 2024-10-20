import pygame
import random
from constants import *

class Fruit:
	def __init__(self):
		self.width = int(SCREEN_WIDTH / 10)
		self.height = int(SCREEN_HEIGHT / 10)
		self.x_position = random.randrange(0, SCREEN_WIDTH, self.width)
		self.y_position = random.randrange(0, SCREEN_HEIGHT, self.height)
		self.rect = pygame.Rect(self.x_position, self.y_position, self.width, self.height)

	def draw(self, surface):
		pygame.draw.rect(surface, "red", self.rect)

	def move(self, snake):
		while True:
			self.rect.left = random.randrange(0, SCREEN_WIDTH, self.width)
			self.rect.top = random.randrange(0, SCREEN_HEIGHT, self.height)

			if self.rect.collidelist(snake) == -1:
				break