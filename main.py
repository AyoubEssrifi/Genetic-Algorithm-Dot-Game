import pygame as pg
import random
import dots
import population
import math
import bar
vec = pg.math.Vector2

############ Some color codes  ############

WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
TEXTCOLOR = (0,   0,  0)
###########################################

(width,height)=(800,800)
dotStartPos = (width/2, height/2)
goalPos = (int(width/2), 0)
alldotsaredead = False
running = True


# Initiliaze pygame #
pg.init()
FONT = pg.font.Font("freesansbold.ttf", 15)
clock = pg.time.Clock()
# Make screen and filling it with color
window = pg.display.set_mode((width, height))

# Create dots group and obstacle 
dotssprite = pg.sprite.Group()
obstacle = pg.sprite.Group()

# goaldotsprite = pg.sprite.Group()

# Creating dots and obstacles
my_population = population.Population(500,(400,700),window,1000,0)
my_dots = my_population.my_dots
my_bar1 = bar.Bar((200,500),window)
my_bar2 = bar.Bar((600,350),window)
my_bar3 = bar.Bar((200,200),window)
# Add the moving bar
# my_bar = bar.Bar((400,400),window)
# dotssprite.add(my_bar)

[dotssprite.add(d) for d in my_dots]
obstacle.add(my_bar1)
obstacle.add(my_bar2)
obstacle.add(my_bar3)



# Function to update screen
def udpatescreen():
	global my_population, dotssprite
	window.fill(WHITE)
	text_count_surf = FONT.render("Gen : " + str(my_population.gen), True, BLACK)
	text_count_rect = text_count_surf.get_rect(center=(70, 30))
	window.blit(text_count_surf, text_count_rect)
	pg.draw.circle(window, RED, goalPos, 10)

	dotssprite.draw(window)
	obstacle.draw(window)
	block(my_bar1)
	block(my_bar2)
	block(my_bar3)
	pg.display.update()
	
# Function to reset screen
def resetscreen():
	global my_population, my_dots, dotssprite
	window.fill(WHITE)
	pg.draw.circle(window, RED, goalPos, 10)

	dotssprite.empty()
	my_dots = my_population.my_dots
	[dotssprite.add(d) for d in my_dots]
	dotssprite.draw(window)
	obstacle.draw(window)

	


# Function to update dots sprite
def rundots():
	global my_population, dotssprite
	# my_population.move()
	dotssprite.update()
	obstacle.update()

# Function to check collision
def check_collision(sp1,sp2):
	return pg.sprite.collide_rect(sp1, sp2)

# Function to block dots with obstacle
def block(ob1):
	for d in dotssprite:
		check = check_collision(ob1, d)
		if check:
			d.dead = True	

while running:
	clock.tick(60)
	for event in pg.event.get():
		if event.type==pg.QUIT:
			running = False
			
	if my_population.allDotsDead() is False:
		rundots()
	else:
		my_population.calculatefitness()
		my_population.naturalselection()
		my_population.mutatedembabies()
		resetscreen()
	udpatescreen()
			
	
	

