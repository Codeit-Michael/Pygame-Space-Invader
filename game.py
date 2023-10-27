import pygame
from settings import WIDTH, HEIGHT, LIFE_SIZE

class Game:
	def __init__(self, screen):
		self.screen = screen

	def show_life(self, life):
		life_size = 30
		img_path = "assets/life/life.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))
		life_x = LIFE_SIZE // 2

		for life in range(life):
			self.screen.blit(life_image, (life_x, HEIGHT + (LIFE_SIZE // 2)))
			life_x += life_size