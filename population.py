import pygame as pg
import dots
import random
import math

class Population():
	def __init__(self,size,startpos,window,step,id):
		self.size = size
		self.gen = 1
		self.my_dots = []
		self.id = id
		self.step = step
		(x,y) = startpos
		for i in range(size):
			self.my_dots.append(dots.Dots((255,255,255),x,y,5,window,i,self.step))
# This is what causes me the problem aaaaaaaaaaaaaahhhh
	# def	move(self):
	# 	for d in self.my_dots:
	# 		d.move(random.uniform(0,2*math.pi))

	def calculatefitness(self):
		for d in self.my_dots:
			d.calculatefitness()

	def allDotsDead(self):
		for d in self.my_dots:
			if (not d.dead) and (not d.reachedgoal):
				return False
		return True	

	def naturalselection(self):
		self.newdots = []
		self.calculateFitnessSum()

		self.best = self.getbestdot()
		self.bestdot = self.best.gimmebaby()
		self.bestdot.isbest = True
		self.bestdot.brain.step = 0
		self.newdots.append( self.bestdot )

		for i in range(len(self.my_dots)-1):
			# Select parent based on fitness
			self.parent = self.selectparent()
			# Get a baby
			self.baby = self.parent.gimmebaby()
			self.newdots.append(self.baby)
		self.my_dots = self.newdots
		self.gen += 1
		self.id += 1

	def calculateFitnessSum(self):
		self.fitnesssum = 0
		for d in self.my_dots:
			self.fitnesssum += d.fitness	

	def selectparent(self):
		self.rand = random.uniform(0,self.fitnesssum)
		self.runningsum = 0
		for d in self.my_dots:
			self.runningsum += d.fitness
			if self.runningsum > self.rand:
				return d
		# Should never go to this point		
		return None

	def mutatedembabies(self):
		for i in range(1,len(self.my_dots)-1):
			# print("old brain: ",d.brain.directions)
			self.my_dots[i+1].brain.mutate()
			# print("new brain: ",d.brain.directions)

	def getbestdot(self):
		max = 0
		max_idx = 0
		for i in range(len(self.my_dots)):
			if self.my_dots[i].fitness > max:
				max = self.my_dots[i].fitness
				max_idx	= i
		if self.my_dots[max_idx].reachedgoal:
			self.step = self.my_dots[max_idx].brain.step
		return self.my_dots[max_idx]			
				


