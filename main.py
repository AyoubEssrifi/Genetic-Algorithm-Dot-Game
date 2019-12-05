
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
pause = False
score = 0

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

	text_count_surf = FONT.render("Score : " + str(score), True, BLACK)
	text_count_rect = text_count_surf.get_rect(center=(70, 60))
	window.blit(text_count_surf, text_count_rect)

	pausefont = pg.font.Font('freesansbold.ttf',20)
	pausesurf, pauserect = text_objects("Press P to pause", pausefont)
	pauserect.center = (700,30)
	window.blit(pausesurf, pauserect)

	pg.draw.circle(window, RED, goalPos, 10)
	dotssprite.draw(window)
	obstacle.draw(window)
	block(my_bar1)
	block(my_bar2)
	block(my_bar3)
	pg.display.update()
	
# Function to reset screen
def resetscreen():
	global my_population, my_dots, dotssprite, scores
	score = 0
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

# Function to make text in screen			
def text_objects(text, font):
	textSurface = font.render(text, True, BLACK)
	return textSurface, textSurface.get_rect()

# Function to make interactive buttons
def button(text,posx,posy,width,height,size,action):

	# Getting mouse informations
	mousepos = pg.mouse.get_pos()
	click = pg.mouse.get_pressed()
	if posx < mousepos[0] < posx + width and posy < mousepos[1] < posy + height:
		if click[0] == 1 and action != None:
			action()
	else:		
		pg.draw.rect(window,WHITE,[posx,posy,width,height])
	font = pg.font.Font('freesansbold.ttf',size)
	surf, rect = text_objects(text, font)
	rect.center = (posx+int(width/2),posy+int(height/2))
	window.blit(surf,rect)

# Game intro screen
def game_intro():
	intro =True
	while intro:
		clock.tick(60)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()
		window.fill(WHITE)

		# Displaying Text in the start menu
		largeText = pg.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = text_objects("AI Dot Game", largeText)
		TextRect.center = (int((width/2)),int((height/2)))
		window.blit(TextSurf, TextRect)

		# Making start menu buttons
		button("Start Game",250,600,300,50,50,game_running)

		pg.display.update()	

# Function to pause the game
def paused():
	clock.tick(60)
	while pause:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()
		window.fill(WHITE)
		pausefont = pg.font.Font('freesansbold.ttf',80)
		pausesurf, pauserect = text_objects("Game Paused", pausefont)
		pauserect.center = (int((width/2)),int((height/2)))
		window.blit(pausesurf,pauserect)
		button("Continue",250,600,300,50,50,unpause)
		pg.display.update()	

# Function to unpause the game
def unpause():
	pause = False
	game_running()

# Function to calculate the score : number of dot reaching the goal
def count_score():
	global score
	idx = []
	for i in range(len(my_dots)):
		if i not in idx:
			if my_dots[i].reachedgoal:
				score += 1
				idx.append(i)			

# Function to run the game
def game_running():
	global running, pause, score
	while running:
		clock.tick(60)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_p:
					pause = True
					paused()
		count_score()								
		if my_population.allDotsDead() is False:
			rundots()
		else:
			my_population.calculatefitness()
			my_population.naturalselection()
			my_population.mutatedembabies()
			resetscreen()
		udpatescreen()
		score = 0
			
game_intro()	
	

