import pygame
from fruit import Fruit
from constants import *

pygame.font.init()

font = pygame.font.Font(None, 32)

class Player:
	def __init__(self, difficulty, color):
		self.width = int(SCREEN_WIDTH / 10)
		self.height = int(SCREEN_HEIGHT / 10)
		self.head = pygame.Rect(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), self.width, self.height)
		self.color = color
		self.body = []
		self.direction = None
		self.new_direction = None
		self.move_buffer = []
		self.move_speed = difficulty
		self.move_cooldown = self.move_speed
		self.score = 0

	def update(self, events, delta_time):
		colliding = self.is_colliding_self()

		out_of_bounds = self.is_out_of_bounds()

		for event in events:
			if event.type != pygame.KEYDOWN:
				continue
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				self.move_buffer.append("UP")
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				self.move_buffer.append("DOWN")
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				self.move_buffer.append("RIGHT")
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				self.move_buffer.append("LEFT")

		self.move_buffer = self.move_buffer[-2:]

		self.move(delta_time)

		return colliding, out_of_bounds

	def draw(self, surface: pygame.surface.Surface):
		if self.direction == None:
			directions_text = font.render("Use WASD or Arrow Keys to move", True, "white", "grey10")
			surface.blit(source=directions_text, dest=((SCREEN_WIDTH / 2) - (directions_text.get_width() / 2), 144))

		for segment in self.body:
			pygame.draw.rect(surface, "darkgray", segment)
		pygame.draw.rect(surface, self.color, self.head)

		score_text = font.render(f"Score: {self.score}", True, "white")
		surface.blit(source=score_text, dest=((SCREEN_WIDTH / 2) - (score_text.get_width() / 2), 10))

	def move(self, delta_time):
		self.move_cooldown -= delta_time

		if self.move_cooldown > 0:
			return
		
		if len(self.move_buffer) > 0:
			self.new_direction = self.move_buffer.pop(0)
		
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

	def is_colliding_fruit(self, fruit: Fruit):
		if not self.head.colliderect(fruit):
			return
		
		self.grow()
		if len(self.body) >= ((SCREEN_WIDTH / self.width) * (SCREEN_HEIGHT / self.height)):
			return

		fruit.move([self.head] + self.body)

	def is_colliding_self(self):
		return 0 < self.head.collidelist(self.body)
	
	def is_out_of_bounds(self):
		display = pygame.display.Info()
		return not (0 <= self.head.centerx <= display.current_w and 0 <= self.head.centery <= display.current_h)