import time, pygame

COLOR_BG = (10, 10, 10)
BALL_COLOR = (255, 0, 0)
X = 400
Y = 300
VX = 0.5
VY = 0.5

pygame.init()
screen = pygame.display.set_mode((800, 600))


while True:
    screen.fill(COLOR_BG)
    pygame.draw.circle(screen, BALL_COLOR, (X, Y), 10, 0)
    pygame.display.update()
    X += VX
    Y += VY

    if (X == 10 and Y == 10) or (X == 10 and Y == 590) or (X == 790 and Y == 10) or (X == 790 and Y == 590):
        VX = -VX
        VY = -VY
    elif X == 10 or X == 790:
        VX = -VX
    elif Y == 10 or Y == 590:
        VY = -VY
    time.sleep(0.001)
