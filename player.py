import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.x = pos[0]
		self.y = pos[1]
		self.rect = pygame.Rect(self.x, self.y, size, size)
		self.color = pygame.Color("red")
		self.player_speed = 3

		# player status
		self.life = 5

	def move_left(self):
		self.rect.x -= self.player_speed

	def move_up(self):
		self.rect.y -= self.player_speed

	def move_right(self):
		self.rect.x += self.player_speed

	def move_bottom(self):
		self.rect.y += self.player_speed

	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)