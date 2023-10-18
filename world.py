import pygame
from player import Player
from settings import HEIGHT, WIDTH, player_size, border_thickness, nav_thickness
from game import Game

class World:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False

		self.players = pygame.sprite.Group()
		self.game = Game(self.screen)

		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		player_x, player_y = WIDTH // 2, HEIGHT - (player_size * 2) 
		center_size = player_size // 2
		player_pos = (player_x - center_size, player_y - center_size)
		self.player = Player(player_pos, player_size)

	def add_additionals(self):
		# add nav
		nav = pygame.Rect(0, HEIGHT, WIDTH, nav_thickness)
		pygame.draw.rect(self.screen, pygame.Color("gray"), nav)

	def player_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] or keys[pygame.K_LEFT]:
			if self.player.rect.left >= 0:
				self.player.move_left()
		if keys[pygame.K_w] or keys[pygame.K_UP]:
			if self.player.rect.top >= 0:
				self.player.move_up()
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			if self.player.rect.right <= WIDTH:
				self.player.move_right()
		if keys[pygame.K_s] or keys[pygame.K_DOWN]:
			if self.player.rect.bottom <= HEIGHT:
				self.player.move_bottom()

	def update(self):
		# add nav
		self.add_additionals()
		
		self.player.update(self.screen)
		self.game.show_life(self.player)
