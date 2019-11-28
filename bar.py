import pygame as pg

vec = pg.math.Vector2

class Bar(pg.sprite.Sprite):
	def __init__(self,startpos,window):
		pg.sprite.Sprite.__init__(self)
		self.window = window
		self.image = pg.Surface((400,20),pg.SRCALPHA)
		self.pos = vec(startpos)
		self.vel =vec(3,0)
		self.maxspeed = 3
		self.rect = self.image.get_rect(center=self.pos)
		self.image.fill((255,0,0))
		self.touch_right = False
		self.touch_left = False


	# def update(self):
	# 	if self.vel.length() > self.maxspeed:
	# 		self.vel.scale_to_length(self.maxspeed)
	# 	self.rect.move_ip(self.vel)
	# 	if self.rect.right > 800 or self.rect.left < 0:
	# 		self.vel *= -1
		# self.rect = self.image.get_rect(center=self.pos)		


