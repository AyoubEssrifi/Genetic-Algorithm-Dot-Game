import pygame as pg
import random
import math

class Brain():

	def __init__(self,size):
		self.size=size
		self.directions=[]
		self.step=0

	def randomize(self):
		for i in range(self.size):
			randomangle=random.uniform(0,2*math.pi)
			self.directions.append(randomangle)

	def clone(self):
		self.brainclone = Brain(self.size)
		# print("old directions",self.directions)
		for d in self.directions:
			self.brainclone.directions.append(d)
		# print("new directions",self.brainclone.directions)	
		return self.brainclone
		
	def mutate(self):
		self.mutationrate = 0.01
		for i in range(len(self.directions)):
			self.rand = random.uniform(0,1)
			if self.rand < self.mutationrate:
				self.directions[i] = random.uniform(0,2*math.pi)



		


