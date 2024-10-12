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
screen = pygame.display.set_mode(size=(pygame.display.Info().current_w, pygame.display.Info().current_h), flags=pygame.FULLSCREEN)

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

	if len([player.head] + player.body) >= (screen.get_width() / 40) * (screen.get_height() / 40):
		menu.gameOverMenu(player.score)

def draw():
	screen.fill(color="grey10")
	fruit.draw(screen)
	player.draw(screen)
	menu.draw()

def startGame():
	global player
	global fruit
	player = Player(x_position=screen.get_width() / 2, y_position=screen.get_height() / 2, width=40, height=40)
	fruit = Fruit(x_position=random.randrange(0, screen.get_width() - 40, 40), y_position=random.randrange(0, screen.get_height() - 40, 40), width=40, height=40)
	menu.close()

menu = GameMenu(surface=screen, start_function=startGame)

player = Player(x_position=screen.get_width() / 2, y_position=screen.get_height() / 2, width=40, height=40)
fruit = Fruit(x_position=random.randrange(0, screen.get_width() - 40, 40), y_position=random.randrange(0, screen.get_height() - 40, 40), width=40, height=40)

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