import pygame
import pygame_menu
import pygame_menu.events
import pygame_menu.locals
import pygame_menu.menu
import pygame_menu.themes
import pygame_menu.widgets
import pygame_menu.widgets.selection
import pygame_menu.widgets.selection.simple
from constants import *

pygame.font.init()
score_font = pygame.font.Font(None, 32)

class GameMenu:
	def __init__(self, surface: pygame.Surface, start_function):
		self.surface = surface

		self.theme = pygame_menu.themes.THEME_DARK.copy()
		self.theme.title_font_size = 56
		self.theme.widget_font_size = 40
		self.theme.widget_font_color = pygame.Color(225, 225, 225, 255)
		self.theme.selection_color = pygame.Color(75, 255, 75, 255)
		self.theme.widget_selection_effect = pygame_menu.widgets.selection.simple.SimpleSelection()
		self.theme.widget_font_shadow = True
		self.theme.widget_font_shadow_offset = 2
		self.alt_theme = self.theme.copy().set_background_color_opacity(0.8)

		self.main_menu = pygame_menu.menu.Menu(title="Main Menu", menu_id="main_menu", width=self.surface.get_width(), height=surface.get_height(), theme=self.theme)
		self.pause_menu = pygame_menu.menu.Menu(title="Game Paused", menu_id="pause_menu", width=surface.get_width(), height=surface.get_height(), theme=self.alt_theme)
		self.game_over_menu = pygame_menu.menu.Menu(title="Game Over", menu_id="pause_menu", width=surface.get_width(), height=surface.get_height(), theme=self.alt_theme)
		self.player_score = 0

		self.main_menu.add.button(title="Play", action=start_function)
		self.main_menu.add.vertical_margin(margin=self.main_menu.get_widgets()[0].get_size()[1])
		self.main_menu.add.button(title="Exit", action=pygame_menu.events.EXIT)

		self.pause_menu.add.button(title="Resume", action=self.close)
		self.pause_menu.add.vertical_margin(margin=self.pause_menu.get_widgets()[0].get_size()[1])
		self.pause_menu.add.button(title="Main Menu", action=self.mainMenu)

		self.game_over_menu.add.button(title="Replay", action=start_function)
		self.game_over_menu.add.vertical_margin(margin=self.game_over_menu.get_widgets()[0].get_size()[1])
		self.game_over_menu.add.button(title="Main Menu", action=self.mainMenu)
		self.game_over_menu.add.vertical_margin(margin=self.game_over_menu.get_widgets()[0].get_size()[1])
		self.game_over_menu.add.button(title="Exit", action=pygame_menu.events.EXIT)

		self.menus = [self.main_menu, self.pause_menu, self.game_over_menu]

		self.current_menu = self.main_menu

	def update(self, events):
		for event in events:
			if event.type == pygame.VIDEORESIZE:
				for menu in self.menus:
					menu.resize(width=self.surface.get_width(), height=self.surface.get_height())
		if self.current_menu != None:
			widget = self.current_menu.get_mouseover_widget()
			if widget != None:
				self.current_menu.unselect_widget()
				widget.select(True, True)
			self.current_menu.update(events)
			
	def draw(self):
		if self.current_menu == None:
			return
		
		self.current_menu.draw(surface=self.surface)

		if self.current_menu == self.game_over_menu:
			score_text = score_font.render(f"Final Score: {self.player_score}", True, "white")
			self.surface.blit(source=score_text, dest=((self.surface.get_width() / 2) - (score_text.get_width() / 2), 15))

	def mainMenu(self):
		self.current_menu.unselect_widget()
		self.current_menu = self.main_menu
		self.current_menu.select_widget(self.current_menu.get_widgets()[0])

	def pauseMenu(self):
		if self.current_menu == self.main_menu:
			return
		if self.current_menu == self.pause_menu:
			self.close()
			return
		self.current_menu = self.pause_menu
		self.current_menu.select_widget(self.current_menu.get_widgets()[0])

	def gameOverMenu(self, player_score):
		self.player_score = player_score

		self.current_menu = self.game_over_menu
		self.current_menu.select_widget(self.current_menu.get_widgets()[0])

	def close(self):
		self.current_menu = None