import pygame
pygame.init()
sw, sh = 500, 500
screen = pygame.display.set_mode((sw, sh))
font = pygame.font.Font(None, 36)
text = font.render("my first game rectangal", True, pygame.Color("black"))
text_rect = text.get_rect(center=(sw // 2, sh // 2 + 110))
rect_color = (0,0,255)
rect = pygame.Rect(100,100,200,100)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 255, 0))
    pygame.draw.rect(screen,rect_color,rect)
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()