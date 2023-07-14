import pygame
from settings import WIDTH, HEIGHT, border_thickness

class Game:
	def __init__(self, screen):
		self.screen = screen

	def show_life(self, player):
		life_size = 30
		img_path = "assets/life/life.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))

		if player.rect.x < WIDTH // 2:
			life_x = border_thickness // 2
		else:
			life_x = WIDTH // 2 + border_thickness

		for life in range(player.life):
			self.screen.blit(life_image, (life_x, HEIGHT + (border_thickness // 2)))
			life_x += life_size