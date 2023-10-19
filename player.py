import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.x = pos[0]
		self.y = pos[1]

		# player 
		img_path = 'assets/ship/ship.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)
		self.mask = pygame.mask.from_surface(self.image)
		self.player_speed = 4

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

	def update(self):
		self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))