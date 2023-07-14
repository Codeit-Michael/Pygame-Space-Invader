import pygame
from player import Player
from settings import HEIGHT, WIDTH, player_size, border_thickness
from game import Game

class World:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False
		self.player_speed = 3

		self.color = pygame.Color("indigo")
		self.boundary = pygame.Rect(WIDTH // 2 - (border_thickness // 2), 0, border_thickness, HEIGHT)
		self.game = Game()

		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		player_x, player_y = WIDTH // 4, HEIGHT // 2
		center_size = player_size // 2
		posA, posB = (player_x - center_size, player_y - center_size), ((player_x * 3) - center_size, player_y - center_size)
		self.playerA = Player(posA, player_size)
		self.playerB = Player(posB, player_size)
		# self.players.add(playerA)
		# self.players.add(playerB)

	def _player_move(self):
		keys = pygame.key.get_pressed()
		center_size = border_thickness // 2

		if keys[pygame.K_a]:
			if self.playerA.rect.left > 0:
				self.playerA.rect.x -= self.player_speed
		if keys[pygame.K_w]:
			if self.playerA.rect.top > 0:
				self.playerA.rect.y -= self.player_speed
		if keys[pygame.K_d]:
			if self.playerA.rect.right < self.boundary.left:
				self.playerA.rect.x += self.player_speed
		if keys[pygame.K_s]:
			if self.playerA.rect.bottom < HEIGHT:
				self.playerA.rect.y += self.player_speed

		if keys[pygame.K_LEFT]:
			if self.playerB.rect.left > self.boundary.right:
				self.playerB.rect.x -= self.player_speed
		if keys[pygame.K_UP]:
			if self.playerB.rect.top > 0:
				self.playerB.rect.y -= self.player_speed
		if keys[pygame.K_RIGHT]:
			if self.playerB.rect.right < WIDTH:
				self.playerB.rect.x += self.player_speed
		if keys[pygame.K_DOWN]:
			if self.playerB.rect.bottom < HEIGHT:
				self.playerB.rect.y += self.player_speed

	def update(self):
		pygame.draw.rect(self.screen, self.color, self.boundary)
		self.game.show_life(self.screen)
		self.playerA.update(self.screen)
		self.playerB.update(self.screen)