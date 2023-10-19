import pygame
from ship import Ship
from alien import Alien
from settings import HEIGHT, WIDTH, player_size, enemy_size, border_thickness, nav_thickness
from game import Game

class World:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False

		self.player = pygame.sprite.GroupSingle()
		self.alien = pygame.sprite.Group()
		self.game = Game(self.screen)

		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		# create the player's ship
		player_x, player_y = WIDTH // 2, HEIGHT - (player_size * 2) 
		center_size = player_size // 2
		player_pos = (player_x - center_size, player_y - center_size)
		self.player.add(Ship(player_pos, player_size))

		# create enemy's/alien's ship
			# enemy random spawning should be regulated as long as player not died yet (spawn delay: 3 secs)
			# could also work for one-time spawn
			# could also be if one pattern spawn, and only repeat spawn once first set is done
		enemy_x, enemy_y = WIDTH // 2, HEIGHT // 4 
		center = enemy_size // 2
		enemy_pos = (enemy_x - center, enemy_y - center)
		self.alien.add(Alien(enemy_pos, enemy_size))

	def add_additionals(self):
		# add nav
		nav = pygame.Rect(0, HEIGHT, WIDTH, nav_thickness)
		pygame.draw.rect(self.screen, pygame.Color("gray"), nav)

	def player_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] or keys[pygame.K_LEFT]:
			if self.player.sprite.rect.left >= 0:
				self.player.sprite.move_left()
		if keys[pygame.K_w] or keys[pygame.K_UP]:
			if self.player.sprite.rect.top >= 0:
				self.player.sprite.move_up()
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			if self.player.sprite.rect.right <= WIDTH:
				self.player.sprite.move_right()
		if keys[pygame.K_s] or keys[pygame.K_DOWN]:
			if self.player.sprite.rect.bottom <= HEIGHT:
				self.player.sprite.move_bottom()

	def update(self):
		# add nav
		self.add_additionals()
		
		self.player.update()
		self.player.draw(self.screen)

		# alien rendering
		self.alien.draw(self.screen)

		self.game.show_life(self.player.sprite.life)
