import pygame
from ship import Ship
from alien import Alien
from settings import HEIGHT, WIDTH, CHARACTER_SIZE, BULLET_SIZE, NAV_THICKNESS
from bullet import Bullet
from game import Game

class World:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False

		self.player = pygame.sprite.GroupSingle()
		self.aliens = pygame.sprite.Group()
		self.enemy_bullets = pygame.sprite.Group()
		self.game = Game(self.screen)

		self._generate_world()

		
	# create and add player to the screen
	def _generate_world(self):
		# create the player's ship
		player_x, player_y = WIDTH // 2, HEIGHT - CHARACTER_SIZE
		center_size = CHARACTER_SIZE // 2
		player_pos = (player_x - center_size, player_y)
		self.player.add(Ship(player_pos, CHARACTER_SIZE))

		# generate opponents
		enemy_cols = (WIDTH // CHARACTER_SIZE) // 2
		enemy_rows = 3
		for y in range(enemy_rows):
			for x in range(enemy_cols):
				my_x = CHARACTER_SIZE * x
				my_y = CHARACTER_SIZE * y
				specific_pos = (my_x, my_y)
				self.aliens.add(Alien(specific_pos, CHARACTER_SIZE, y))


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
			self.player.sprite._shoot()


	def _detect_collisions(self):
		player_attack_collision = pygame.sprite.groupcollide(self.aliens, self.player.sprite.player_bullets, True, True)
		enemy_attack_collision = pygame.sprite.groupcollide(self.player, self.enemy_bullets, False, True)

		if player_attack_collision:
			pass
			# print(True) # make this condition add score
		if enemy_attack_collision:
			pass
			# print(False) # make this decrease life by 1


	def _alien_movement(self):
		move_sideward = False
		move_forward = False

		for alien in self.aliens.sprites():
			if alien.to_direction == "right" and alien.rect.right < WIDTH or alien.to_direction == "left" and alien.rect.left > 0:
				move_sideward = True
				move_forward = False
			else:
				move_sideward = False
				move_forward = True
				alien.to_direction = "left" if alien.to_direction == "right" else "right"
				break

		for alien in self.aliens.sprites():
			if move_sideward and not move_forward:
				if alien.to_direction == "right":
					alien.move_right()
				if alien.to_direction == "left":
					alien.move_left()
			if not move_sideward and move_forward:
					alien.move_bottom()

###
	def _alien_shoot(self):
		for alien in self.aliens.sprites():
			if (WIDTH - alien.rect.x) // CHARACTER_SIZE == (WIDTH - self.player.sprite.rect.x) // CHARACTER_SIZE:
				specific_pos = (alien.rect.centerx - (BULLET_SIZE // 2), alien.rect.centery)
				self.enemy_bullets.add(Bullet(specific_pos, BULLET_SIZE, "enemy"))
				break

	def update(self):
		# detecting if bullet, alien, and player group is colliding
		self._detect_collisions()

		# allows the aliens to move
		self._alien_movement()

##		# allows alien to shoot the player
		self._alien_shoot()

		# bullets rendering
		self.player.sprite.player_bullets.update()
		self.player.sprite.player_bullets.draw(self.screen)

		self.enemy_bullets.update()
		self.enemy_bullets.draw(self.screen)

		# player ship rendering
		self.player.update()
		self.player.draw(self.screen)

		# alien rendering
		self.aliens.draw(self.screen)

		# add nav
		self.add_additionals()