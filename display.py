import pygame
from settings import WIDTH, HEIGHT, SPACE, FONT_SIZE

pygame.font.init()

class Display:
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont("monospace", FONT_SIZE)
		self.message_color = pygame.Color("blue")


	def nav_board(self):
		pass

	def show_life(self, life):
		life_size = 30
		img_path = "assets/life/life.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))
		life_x = SPACE // 2

		if life != 0:
			for life in range(life):
				self.screen.blit(life_image, (life_x, HEIGHT + (SPACE // 2)))
				life_x += life_size

	def show_score(self, score):
		score_x = WIDTH // 3
		score = self.font.render(f'score: {score}', True, self.message_color)
		self.screen.blit(score, (score_x, (HEIGHT + (SPACE // 2))))

	def _show_level(self):
		pass