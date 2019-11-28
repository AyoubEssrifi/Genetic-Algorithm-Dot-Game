import pygame as pg
import random
import brain
import math
vec = pg.math.Vector2

class Dots(pg.sprite.Sprite):
	def __init__(self,color,x,y,radius,window,id,step):
		pg.sprite.Sprite.__init__(self)
		self.maxspeed = 6
		self.window = window
		self.id = id
		self.color = color
		self.x = x
		self.y = y
		self.pos = vec (self.x,self.y)
		self.radius = radius
		self.step = step
		self.id = id
		self.image = pg.Surface((10,10),pg.SRCALPHA)
		# Create an image in sprite
		# self.image = pg.image.load('binom.jpg').convert_alpha()
		# self.size = self.image.get_size()
		# self.small = pg.transform.scale(self.image, (int(self.size[0]/10),int(self.size[1]/10)))
		# self.image = self.small
		self.rect = self.image.get_rect(center=self.pos)
		self.image.fill(color)
		#pg.draw.circle(self.image,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),(5,5),self.radius)
		# pg.draw.ellipse(self.image,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),[0, 0, 10, 10],0)
		self.vel = vec(0, 0)	
		self.accel = vec(0, 0)
		self.dead = False
		self.brain = brain.Brain(step)
		self.brain.randomize()
		self.reachedgoal = False
		self.isbest = False
		self.minstep = self.step

	def move(self,angle):
		# self.update()
		if self.dead or self.reachedgoal:
			self.rect.clamp_ip(self.window.get_rect())
		else:
			if self.vel.length() > self.maxspeed:
				self.vel.scale_to_length(self.maxspeed)
			if self.brain.step < len(self.brain.directions) - 1:
				self.accel = [math.cos(angle), math.sin(angle)]
				self.step += 1
			else:
				self.dead = True
			self.vel += self.accel
			self.pos += self.vel
			self.rect.center = self.pos
			self.brain.step += 1

	def update(self):
		self.drawdot()
		if (not self.dead) and (not self.reachedgoal):
			self.move(self.brain.directions[self.brain.step])
			if self.pos.x < 0 or self.pos.x > self.window.get_width() or self.pos.y < 2 or self.pos.y > self.window.get_height():
				self.dead = True
			# if (300 < self.pos.y < 315) and (0 < self.pos.x < 600):
			# 	self.dead = True	
			if self.pos.distance_to(vec((400, 0))) < 15:  # Change pos of goal if goal changed
				self.reachedgoal = True
			if self.brain.step > self.minstep:
				self.dead = True
		

	def calculatefitness(self):
		if self.reachedgoal :
			self.distanceTogoal = self.pos.distance_to(vec((self.window.get_width()/2), 0))
			self.fitness = 1/16+10000/(self.step*self.step)
		else:
			self.distanceTogoal = self.pos.distance_to(vec((self.window.get_width()/2), 0))
			self.fitness = 1/(self.distanceTogoal*self.distanceTogoal)	


	def gimmebaby(self):
		self.baby = Dots((255,255,255),self.x,self.y,5,self.window,self.id,self.step) # A revoir
		self.baby.brain = self.brain.clone()
		return self.baby

	def drawdot(self):
		if self.isbest:
			pg.draw.ellipse(self.image,(0,255,0),[0, 0, 10, 10],0)
		else:
			pg.draw.ellipse(self.image,(0,0,0),[0, 0, 10, 10],0)

		


