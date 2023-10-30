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
		self.aliens = pygame.sprite.Group()
		self.player_bullets = pygame.sprite.Group()
		self.enemy_bullets = pygame.sprite.Group()
		self.game = Game(self.screen)

		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		# create the player's ship
		player_x, player_y = WIDTH // 2, HEIGHT - PLAYER_SIZE
		center_size = PLAYER_SIZE // 2
		player_pos = (player_x - center_size, player_y)
		self.player.add(Ship(player_pos, PLAYER_SIZE))

		# generate opponents
		enemy_cols = (WIDTH // ENEMY_SIZE) // 2
		enemy_rows = 3
		for y in range(enemy_rows):
			for x in range(enemy_cols):
				my_x = ENEMY_SIZE * x
				my_y = ENEMY_SIZE * y
				specific_pos = (my_x, my_y)
				self.aliens.add(Alien(specific_pos, ENEMY_SIZE, y))

	def add_additionals(self):
		# add nav bar
		nav = pygame.Rect(0, HEIGHT, WIDTH, NAV_THICKNESS)
		pygame.draw.rect(self.screen, pygame.Color("gray"), nav)

		# show player's life
		self.game.show_life(self.player.sprite.life)

	def player_move(self, attack = False):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] or keys[pygame.K_LEFT]:
			if self.player.sprite.rect.left > 0:
				self.player.sprite.move_left()
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			if self.player.sprite.rect.right < WIDTH:
				self.player.sprite.move_right()
		# might use these up and down buttons for future versions
		# if keys[pygame.K_w] or keys[pygame.K_UP]:
		# 	if self.player.sprite.rect.top > 0:
		# 		self.player.sprite.move_up()		
		# if keys[pygame.K_s] or keys[pygame.K_DOWN]:
		# 	if self.player.sprite.rect.bottom < HEIGHT:
		# 		self.player.sprite.move_bottom()

		if attack:
			specific_pos = (self.player.sprite.rect.centerx - (BULLET_SIZE // 2), self.player.sprite.rect.y)
			self.player_bullets.add(Bullet(specific_pos, BULLET_SIZE, "player"))

	def _detect_collisions(self):
		player_attack_collision = pygame.sprite.groupcollide(self.aliens, self.player_bullets, True, True)
		enemy_attack_collision = pygame.sprite.groupcollide(self.player, self.enemy_bullets, True, True)

		if player_attack_collision:
			print(True) # make this condition add score
		if enemy_attack_collision:
			print(False) # make this decrease life by 1

	def update(self):
		# detecting if bullet, alien, and player group is colliding
		self._detect_collisions()

		# bullets rendering
		self.player_bullets.update()
		self.player_bullets.draw(self.screen)

		# player ship rendering
		self.player.update()
		self.player.draw(self.screen)

		# alien rendering
		self.aliens.draw(self.screen)

		# add nav
		self.add_additionals()