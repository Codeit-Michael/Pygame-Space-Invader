import pygame
from settings import WIDTH, HEIGHT, nav_thickness, border_thickness

class Game:

	def show_life(self, screen):
		nav = pygame.Rect(0, HEIGHT, WIDTH, nav_thickness)
		nav_border = pygame.Rect((WIDTH // 2) - (border_thickness // 2), HEIGHT, border_thickness, nav_thickness)
		
		pygame.draw.rect(screen, pygame.Color("gray"), nav)
		pygame.draw.rect(screen, pygame.Color("darkslategray"), nav_border)