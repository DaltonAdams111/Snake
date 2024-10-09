import pygame
from constants import *

class Player:
	def __init__(self, x_positon, y_position, width, height):
		self.position = pygame.Vector2(x=x_positon, y=y_position)
		self.width = width
		self.height = height
		self.head = pygame.Rect(x_positon, y_position, width, height)
		self.body = [self.head]
		self.direction = None
		self.new_direction = None
		self.move_cooldown = PLAYER_MOVE_SPEED

	def update(self, delta_time):
		self.move_cooldown -= delta_time

		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.new_direction = "UP"
		if keys[pygame.K_RIGHT]:
			self.new_direction = "RIGHT"
		if keys[pygame.K_DOWN]:
			self.new_direction = "DOWN"
		if keys[pygame.K_LEFT]:
			self.new_direction = "LEFT"

		if self.move_cooldown > 0:
			return
		
		if self.new_direction == "UP" and not self.direction == "DOWN":
			self.direction = "UP"
		if self.new_direction == "RIGHT" and not self.direction == "LEFT":
			self.direction = "RIGHT"
		if self.new_direction == "DOWN" and not self.direction == "UP":
			self.direction = "DOWN"
		if self.new_direction == "LEFT" and not self.direction == "RIGHT":
			self.direction = "LEFT"

		if self.direction == None:
			return
		
		self.head.move_ip(DIRECTIONS[self.direction])
		self.move_cooldown = PLAYER_MOVE_SPEED

	def draw(self, surface):
		pygame.draw.rect(surface, "green", self.head)