import sys, random, pygame, os
from SimpleDrawEngine import *
from astronauts import *


## Limpador de tela multiplataforma Magoninho Gamer versão 1.2
def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')

limpa_tela()


def main(color):
	pygame.init()

	N = 200
	white = (255, 255, 255)
	black = (0,0,0)
	red = (255, 0, 0)
	largura, altura = 800, 600

	screen = pygame.display.set_mode((largura, altura))
	caption = pygame.display.set_caption("ALPHA")

	# posisão das estrelas
	## estrelas menores
	stars = [
		[random.randint(0, largura), random.randint(0, altura)] for x in range(N)
	]
	## estrelas grandes

	big_stars = [
		[random.randint(0, largura), random.randint(0, altura)] for x in range(50)
	]


	pygame.mixer.init()
	pygame.mixer.music.load('sound.ogg')
	pygame.mixer.music.play(-1)

	clock = pygame.time.Clock()
	file = color
	## objetos
	test = 45
	pos_x = -360
	vx = 10
	angle = 0
	player = Player(screen, ("characters/" + file + ".png"), (0, 0), angle, pos_x)
	while True:	
		clock.tick(30)
		angle += 5
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
		screen.fill(black)


		# Drawinings
		## Stars
		for star in stars:
			Rect(screen, white, (star[0], star[1], 2, 2))
			star[0] -= 0.5
			if star[0] < 0:
				star[0] = largura
		for big_star in big_stars:
			Circle(screen, white, (big_star[0], big_star[1]), 3)
			big_star[0] -= 1
			if big_star[0] < 0:
				big_star[0] = largura
		## Astronauts
		player.move(vx)
		player.animation(angle)
		
		pos_x += vx
		vx -= 0.035

		if vx <= 0:
			vx = 0
		
		## Update
		pygame.display.flip()