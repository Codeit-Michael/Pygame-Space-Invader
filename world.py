import pygame
from player import Player
from settings import HEIGHT, WIDTH, player_size, border_thickness, nav_thickness
from game import Game

class World:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False

		self.boundary = pygame.Rect(WIDTH // 2 - (border_thickness // 2), 0, border_thickness, HEIGHT)
		self.players = pygame.sprite.Group()
		self.game = Game(self.screen)

		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		player_x, player_y = WIDTH // 4, HEIGHT // 2
		center_size = player_size // 2
		posA, posB = (player_x - center_size, player_y - center_size), ((player_x * 3) - center_size, player_y - center_size)
		self.playerA = Player(posA, player_size)
		self.playerB = Player(posB, player_size)

	def add_additionals(self):
		# add border
		color = pygame.Color("indigo")
		pygame.draw.rect(self.screen, color, self.boundary)

		# add nav
		nav = pygame.Rect(0, HEIGHT, WIDTH, nav_thickness)
		nav_border = pygame.Rect((WIDTH // 2) - (border_thickness // 2), HEIGHT, border_thickness, nav_thickness)
		pygame.draw.rect(self.screen, pygame.Color("gray"), nav)
		pygame.draw.rect(self.screen, pygame.Color("darkslategray"), nav_border)

	def player_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			if self.playerA.rect.left > 0:
				self.playerA.move_left()
		if keys[pygame.K_w]:
			if self.playerA.rect.top > 0:
				self.playerA.move_up()
		if keys[pygame.K_d]:
			if self.playerA.rect.right < self.boundary.left:
				self.playerA.move_right()
		if keys[pygame.K_s]:
			if self.playerA.rect.bottom < HEIGHT:
				self.playerA.move_bottom()

		if keys[pygame.K_LEFT]:
			if self.playerB.rect.left > self.boundary.right:
				self.playerB.move_left()
		if keys[pygame.K_UP]:
			if self.playerB.rect.top > 0:
				self.playerB.move_up()
		if keys[pygame.K_RIGHT]:
			if self.playerB.rect.right < WIDTH:
				self.playerB.move_right()
		if keys[pygame.K_DOWN]:
			if self.playerB.rect.bottom < HEIGHT:
				self.playerB.move_bottom()

	def update(self):
		# add border and nav
		self.add_additionals()
		
		self.playerA.update(self.screen)
		self.game.show_life(self.playerA)
		
		self.playerB.update(self.screen)
		self.game.show_life(self.playerB)
