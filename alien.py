import pygame

class Alien(pygame.sprite.Sprite):
	def __init__(self, pos, size, row_num):
		super().__init__()
		self.x = pos[0]
		self.y = pos[1]

		# alien info
		img_path = f'assets/aliens/{row_num}.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)
		self.mask = pygame.mask.from_surface(self.image)
		self.move_speed = 5

		# alien status
		self.life = 1

	def move_left(self):
		self.rect.x -= self.move_speed

	def move_up(self):
		self.rect.y -= self.move_speed

	def move_right(self):
		self.rect.x += self.move_speed

	def move_bottom(self):
		self.rect.y += self.move_speed

	def update(self):
		self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))