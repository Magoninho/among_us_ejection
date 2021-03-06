import sys, random, pygame, os
from SimpleDrawEngine import *
from astronauts import *


## Limpador de tela multiplataforma Magoninho Gamer versão 1.2
def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')

limpa_tela()


def main(color, name):
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


	void_sound = pygame.mixer.Sound('sound.ogg')
	void_sound.play(-1)

	vote_typing_sound = pygame.mixer.Sound('vote.ogg')
	impostor_sound = pygame.mixer.Sound('impostor.ogg')
	

	clock = pygame.time.Clock()
	file = color
	## objetos
	test = 45
	pos_x = -360
	vx = 10
	angle = 0
	player = Player(screen, ("characters/" + file + ".png"), (0, 0), angle, pos_x)

	texto = Text(24, False, (255, 255, 255), (0, 0), screen)

	impostor = random.choice([True, False])
	
	final_string = ""
	if name != "":
		text = list(f"{name} was The Impostor") if impostor else list(f"{name} was not The Impostor")
	else:
		text = list(f"{file} was The Impostor") if impostor else list(f"{file} was not The Impostor")
		
	text_complete = False


	counter = -25.0
	i = 0
	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
				
		angle += 5

		screen.fill(black)

		if not text_complete: counter += 0.35

		if counter >= 1 and not text_complete:
			final_string += text[i]
			counter = 0
			i += 1
			if len(final_string) == 1:
				vote_typing_sound.play(-1)
			if len(final_string) == len(text):
				text_complete = True
				vote_typing_sound.stop()
				if impostor:
					impostor_sound.play()
		
		


		texto.draw(final_string, (largura / 2, altura / 2))
		
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
		pygame.display.update()

	pygame.quit()