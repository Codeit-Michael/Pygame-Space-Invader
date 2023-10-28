import pygame
from ship import Ship
from alien import Alien
from settings import HEIGHT, WIDTH, PLAYER_SIZE, ENEMY_SIZE, BULLET_SIZE, NAV_THICKNESS
from bullet import Bullet
from game import Game

class World:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False

		self.player = pygame.sprite.GroupSingle()
		self.alien = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.game = Game(self.screen)

		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		# create the player's ship
		player_x, player_y = WIDTH // 2, HEIGHT - (PLAYER_SIZE * 2) 
		center_size = PLAYER_SIZE // 2
		player_pos = (player_x - center_size, player_y - center_size)
		self.player.add(Ship(player_pos, PLAYER_SIZE))

		# generate opponents
		enemy_cols = (WIDTH // ENEMY_SIZE) // 2
		enemy_rows = 3
		for y in range(enemy_rows):
			for x in range(enemy_cols):
				my_x = ENEMY_SIZE * x
				my_y = ENEMY_SIZE * y
				specific_pos = (my_x, my_y)
				self.alien.add(Alien(specific_pos, ENEMY_SIZE, y))

	def add_additionals(self):
		# add nav
		nav = pygame.Rect(0, HEIGHT, WIDTH, NAV_THICKNESS)
		pygame.draw.rect(self.screen, pygame.Color("gray"), nav)

	def player_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] or keys[pygame.K_LEFT]:
			if self.player.sprite.rect.left > 0:
				self.player.sprite.move_left()
		if keys[pygame.K_w] or keys[pygame.K_UP]:
			if self.player.sprite.rect.top > 0:
				self.player.sprite.move_up()
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			if self.player.sprite.rect.right < WIDTH:
				self.player.sprite.move_right()
		if keys[pygame.K_s] or keys[pygame.K_DOWN]:
			if self.player.sprite.rect.bottom < HEIGHT:
				self.player.sprite.move_bottom()
		if keys[pygame.K_SPACE]:
			specific_pos = (self.player.sprite.rect.centerx, self.player.sprite.rect.y)
			self.bullets.add(Bullet(specific_pos, BULLET_SIZE, "player"))

	def update(self):
		# add nav
		self.add_additionals()
		
		self.bullets.update()
		self.bullets.draw(self.screen)

		self.player.update()
		self.player.draw(self.screen)

		# alien rendering
		self.alien.draw(self.screen)

		self.game.show_life(self.player.sprite.life)
