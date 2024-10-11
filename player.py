import pygame
from constants import *

pygame.font.init()

score_font = pygame.font.Font(None, 32)

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

	def update(self, events, delta_time):
		colliding = self.is_colliding()

		out_of_bounds = self.is_out_of_bounds()

		for event in events:
			if event.type != pygame.KEYDOWN:
				continue
			if event.key == pygame.K_UP:
				self.new_direction = "UP"
			if event.key == pygame.K_DOWN:
				self.new_direction = "DOWN"
			if event.key == pygame.K_RIGHT:
				self.new_direction = "RIGHT"
			if event.key == pygame.K_LEFT:
				self.new_direction = "LEFT"

		self.move(delta_time)

		return colliding, out_of_bounds

	def draw(self, surface: pygame.surface.Surface):
		for segment in self.body:
			pygame.draw.rect(surface, "gray", segment)
		pygame.draw.rect(surface, "green", self.head)

		score_text = score_font.render(f"Score: {self.score}", True, "white")
		surface.blit(source=score_text, dest=((surface.get_width() / 2) - (score_text.get_width() / 2), 10))

	def move(self, delta_time):
		self.move_cooldown -= delta_time

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

	def grow(self):
		if self.direction == None:
			return
		self.body.append(pygame.Rect(self.head.left - DIRECTIONS[self.direction][0], self.head.top - DIRECTIONS[self.direction][1], self.head.width, self.head.height))
		self.score += 1

	def is_colliding(self):
		return 0 < self.head.collidelist(self.body)
	
	def is_out_of_bounds(self):
		display = pygame.display.Info()
		return not (0 <= self.head.centerx <= display.current_w and 0 <= self.head.centery <= display.current_h)