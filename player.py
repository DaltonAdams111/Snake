import pygame
from constants import *

class Player:
	def __init__(self, x_positon, y_position, width, height):
		self.width = width
		self.height = height
		self.head = pygame.Rect(x_positon, y_position, width, height)
		self.body = []
		self.direction = None
		self.new_direction = None
		self.move_speed = 0.2
		self.move_cooldown = self.move_speed
		self.score = 0

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
		if len(self.body) > 0:
			self.body.insert(0, pygame.Rect(self.head.left - DIRECTIONS[self.direction][0], self.head.top - DIRECTIONS[self.direction][1], self.head.width, self.head.height))
			self.body.pop()

		self.move_cooldown = self.move_speed

	def draw(self, surface):
		pygame.draw.rect(surface, "green", self.head)
		for segment in self.body:
			pygame.draw.rect(surface, "gray", segment)

	def grow(self):
		self.body.append(pygame.Rect(self.head.left - DIRECTIONS[self.direction][0], self.head.top - DIRECTIONS[self.direction][1], self.head.width, self.head.height))