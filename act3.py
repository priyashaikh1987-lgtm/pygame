import pygame
pygame.init()
sw, sh = 500, 500
screen = pygame.display.set_mode((sw, sh))
font = pygame.font.Font(None, 36)
text = font.render("my first game screen", True, pygame.Color("black"))
text_rect = text.get_rect(center=(sw // 2, sh // 2 + 110))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((58, 58, 58))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()