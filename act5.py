import pygame
pygame.init()
sw,sh = 500,500
screen = pygame.display.set_mode((sw,sh))
player1 = pygame.Rect(100,200,50,50)
player2 = pygame.Rect(200,100,50,50)
speed = 4
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys =pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= speed
    if keys[pygame.K_s]:
        player1.y += speed 
    if keys[pygame.K_a]:
        player1.x -= speed
    if keys[pygame.K_d]:
        player1.x += speed  
    if keys[pygame.K_UP]:
        player2.y -= speed
    if keys[pygame.K_DOWN]:
        player2.y += speed 
    if keys[pygame.K_LEFT]:
        player2.x -= speed
    if keys[pygame.K_RIGHT]:
        player2.x += speed
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), player1)
    pygame.draw.rect(screen, (0, 0, 255), player2)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()