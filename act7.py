import pygame
import random
SW,SH = 500,400
MOVMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
bg_image = pygame.transform.scale(pygame.image.load("download.jpg"),(SW,SH))
font = pygame.font.SysFont("Times New Roman",FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x = max(min(self.rect.x+x_change,SW-self.rect.width),0)
        self.rect.y = max(min(self.rect.y+y_change,SH-self.rect.height),0)
    def set_color(self, color):
        self.image.fill(color)
screen = pygame.display.set_mode((SW,SH))
pygame.display.set_caption("sprite collision")
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color("pink"),20,30)
sprite1.rect.x ,sprite1.rect.y = random.randint(0,SW - sprite1.rect.width),random.randint(0,SH - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color("darkgreen"),20,30)
sprite2.rect.x ,sprite1.rect.y = random.randint(0,SW - sprite2.rect.width),random.randint(0,SH - sprite1.rect.height)
all_sprites.add(sprite2)

running,won = True,False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*MOVMENT_SPEED
        y_change = (keys[pygame.K_DOWN]-keys[pygame.K_UP])*MOVMENT_SPEED
        sprite1.move(x_change ,y_change)
        if x_change != 0 or y_change != 0:
            sprite1.set_color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
    screen.blit(bg_image,(0,0))
    all_sprites.draw(screen)
    if won:
        win_text = font.render("you win",True,pygame.Color("white"))
        screen.blit(win_text,((SW-win_text.get_width())//2,(SH-win_text.get_height())//2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()