import pygame

WIDTH = 360
HEIGHT = 640
BLACK = (0, 0, 0)
pics = []
for i in range(5):
    pic = pygame.image.load("pics/" + str(i) + ".png")
    pics.append(pygame.transform.scale(pic, (WIDTH, HEIGHT)))

pygame.init()
pygame.display.set_caption("Cat Selfie")
icon = pygame.image.load("pics/ico.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode([360, 640])

index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                index += 1
                if index > 4:
                    index = 0

    screen.fill(BLACK)
    screen.blit(pics[index], pics[index].get_rect())
    pygame.display.flip()

pygame.quit()
