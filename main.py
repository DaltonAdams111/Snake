import pygame
import pygame_menu
import pygame_menu.menu
import pygame_menu.themes
from menu import GameMenu
from player import Player
from constants import *

pygame.init()

pygame.display.set_caption(title="Snake")
screen = pygame.display.set_mode(size=(pygame.display.Info().current_w, pygame.display.Info().current_h), flags=pygame.RESIZABLE | pygame.FULLSCREEN)
#screen = pygame.display.set_mode(size=(pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2), flags=pygame.RESIZABLE)

clock = pygame.time.Clock()
delta_time = 0.0

def update(events, delta_time = 0):
	menu.update(events=events)
	if menu.current_menu == None:
		player.update(delta_time)

def draw():
	screen.fill(color="grey10")
	player.draw(screen)
	menu.draw()

def startGame():
	global player
	player = Player(x_positon=screen.get_width() / 2, y_position=screen.get_height() / 2, width=40, height=40)
	menu.close()

menu = GameMenu(surface=screen, start_function=startGame)

player = Player(x_positon=screen.get_width() / 2, y_position=screen.get_height() / 2, width=40, height=40)

def main():
	global delta_time

	running = True
	while running:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()
				if keys[pygame.K_ESCAPE]:
					menu.pauseMenu()

		update(events, delta_time)
		draw()

		pygame.display.flip()

		delta_time = clock.tick(FPS) / 1000
		#print(clock.get_fps())

if __name__ == "__main__":
	main()