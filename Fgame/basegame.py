#Max 6/22 
# in this file I will coding the base of my game without menu and other features, this will only include the playable game

import os, sys, time, pygame, random, math  
pygame.init()

#colors
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREEN = (0,170,0)
BLUE = (0,100,255)
PURPLE = (85,0,85)
WHITE = (255,255,255)
BLACK = (0,0,0)
#def screen vars 
HEIGHT, WIDTH = 900, 1400
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Max's Game") #Set name of window 
#def game vars
vec = pygame.math.Vector2
ACCELERATION = .7
FRICTION = -0.1
FPS = 60
blocksize = (60,60)
platformsize = (WIDTH-1200,30)
Time = pygame.time.Clock()
#def platform
#https://coderslegacy.com/python/pygame-platformer-game-development/, I learned the class function and how to use it from this
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(platformsize)
        self.surf.fill((RED))
        self.rect = self.surf.get_rect(center = (150, HEIGHT-15))
    def movement(self):
        pass
#def player
class playermodel(pygame.sprite.Sprite):
    def __init__(self): #creates obj, defines vars
        super().__init__()
        self.surf = pygame.Surface(blocksize)
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect()

        self.pos = vec((150, HEIGHT-30))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def movement(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACCELERATION
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACCELERATION
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        self.rect.midbottom = self.pos 
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
           self.vel.y = -15
 
 
    def update(self):
        hits = pygame.sprite.spritecollide(plr ,platforms, False)
        if plr.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1 
plr = playermodel()
plat = platform()
#group inits
Bacisent = pygame.sprite.Group()
Bacisent.add(plat)
Bacisent.add(plr)

platforms = pygame.sprite.Group()
platform.add(plat)
#exit func
def exit():#Will change to return to menu func after 
    pygame.quit()
    sys.exit()
#game loop
game = True
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit key 
            exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                plr.jump()
    SCREEN.fill(BLACK)
    plr.movement()
    for entity in Bacisent: #Puts ents on to screen
        SCREEN.blit(entity.surf, entity.rect)
        entity.movemet()
    pygame.display.update()
    Time.tick(FPS)