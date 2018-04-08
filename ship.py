import pygame

class Ship(object):
	"""init for Ship and its position"""
	def __init__(self, screen):
		self.screen = screen
		
		#load image of the ship and get the sq of it
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#choose position
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#move flag
		self.moving_right = False

	def update(self):
		if self.moving_right:
			self.rect.centerx +=1

	def blitme(self):
		"""draw the plane at the place we choose"""
		self.screen.blit(self.image,self.rect)