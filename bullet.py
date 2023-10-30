import pygame
from settings import BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
	def __init__(self, pos, size, side):
		super().__init__()
		self.x = pos[0]
		self.y = pos[1]

		# bullet info
		img_path = f'assets/bullet/{side}-bullet.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)
		self.mask = pygame.mask.from_surface(self.image)
		self.move_speed = BULLET_SPEED


	def _move_bullet(self):
		self.rect.y -= self.move_speed

	def update(self):
		self._move_bullet()
		self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

		# delete the bullet if it get trough out of the screen
		if self.rect.bottom <= 0:
			self.kill()