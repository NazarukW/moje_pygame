import time, pygame

COLOR_BG = (10, 10, 10)
BALL_COLOR = (255, 0, 0)
X = 400
Y = 300
AY = 0.1
VY = 0.0

pygame.init()
screen = pygame.display.set_mode((800, 600))


while True:
    screen.fill(COLOR_BG)
    pygame.draw.circle(screen, BALL_COLOR, (X, Y), 10, 0)
    pygame.display.update()

    Y += VY
    VY += AY
    if Y >= 590:
        VY = -0.9 * VY

    time.sleep(0.01)
