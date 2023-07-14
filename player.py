import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.x = pos[0]
		self.y = pos[1]
		self.rect = pygame.Rect(self.x, self.y, size, size)
		self.color = pygame.Color("red")

		# player status
		self.direction = pygame.math.Vector2(0, 0)
		self.life = 5

	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)