import sys, random, pygame
from SimpleDrawEngine import *
from astronauts import *
pygame.init()

N = 200

white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
largura, altura = 800, 600

screen = pygame.display.set_mode((largura, altura))
caption = pygame.display.set_caption("ALPHA")

# nao funcionou
# for star in range(N):	
# 	x, y = random.randint(0, largura), random.randint(0, altura)
# 	Rect(screen, (255, 255, 255), (x, y, 1, 1))


stars = [
	[random.randint(0, largura), random.randint(0, altura)] for x in range(N)
]


pygame.mixer.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

## objetos
test = 45

angle = 0
while True:	
	clock.tick(30)
	player = Player(screen, "red.png", (0, 0), angle)
	angle += 5
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(black)


	# Drawinings
	## Stars
	for star in stars:
		Rect(screen, white, (star[0], star[1], 2, 2))
		star[0] -= 0.5
		if star[0] < 0:
			star[0] = 800
	## Astronauts
	# screen.blit(astronaut1, astronaut1_rect)
	player.animation()
	# pygame.draw.rect(screen, white, (325, 225, 174, 174))
	## Update
	pygame.display.flip()
