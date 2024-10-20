import pygame
import pygame_menu
import pygame_menu.menu
import pygame_menu.themes
import sys
import random
from menu import GameMenu
from player import Player
from fruit import Fruit
from constants import *

pygame.init()

pygame.display.set_caption(title="Snake")
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
delta_time = 0.0

def update(events, delta_time):
	menu.update(events=events)

	if menu.current_menu != None:
		return
	
	is_colliding_self, is_out_of_bounds = player.update(events, delta_time)
	if is_colliding_self or is_out_of_bounds:
		menu.gameOverMenu(player.score)

	player.is_colliding_fruit(fruit)

	if len([player.head] + player.body) >= (SCREEN_WIDTH / player.width) * (SCREEN_HEIGHT / player.height):
		menu.gameOverMenu(player.score)

def draw():
	screen.fill(color="grey10")
	fruit.draw(screen)
	player.draw(screen)
	menu.draw()

def startGame():
	global player
	global fruit
	player = Player(x_position=SCREEN_WIDTH / 2, y_position=SCREEN_HEIGHT / 2, width=SCREEN_WIDTH / 10, height=SCREEN_HEIGHT / 10)
	fruit = Fruit(x_position=random.randrange(0, SCREEN_WIDTH - int(SCREEN_WIDTH / 10), int(SCREEN_WIDTH / 10)), y_position=random.randrange(0, SCREEN_HEIGHT - int(SCREEN_HEIGHT / 10), int(SCREEN_HEIGHT / 10)), width=SCREEN_WIDTH / 10, height=SCREEN_HEIGHT / 10)
	menu.close()

menu = GameMenu(surface=screen, start_function=startGame)

player = Player(x_position=SCREEN_WIDTH / 2, y_position=SCREEN_HEIGHT / 2, width=SCREEN_WIDTH / 10, height=SCREEN_HEIGHT / 10)
fruit = Fruit(x_position=random.randrange(0, SCREEN_WIDTH - int(SCREEN_WIDTH / 10), int(SCREEN_WIDTH / 10)), y_position=random.randrange(0, SCREEN_HEIGHT - int(SCREEN_HEIGHT / 10), int(SCREEN_HEIGHT / 10)), width=SCREEN_WIDTH / 10, height=SCREEN_HEIGHT / 10)

def main():
	global delta_time

	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
			if event.type != pygame.KEYDOWN:
				continue
			
			if event.key == pygame.K_ESCAPE:
				menu.pauseMenu()

		update(events, delta_time)
		draw()

		pygame.display.flip()

		delta_time = clock.tick(FPS_CAP) / 1000
		#FPS = clock.get_fps()

if __name__ == "__main__":
	main()