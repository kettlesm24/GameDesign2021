#Max 6/22 
# in this file I will coding the base of my game without menu and other features, this will only include the playable game

import os, sys, time, pygame, random, math, numpy
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
randclr=[(207,206,192),(163,163,161),(205,205,205)]
#def screen vars 
HEIGHT, WIDTH = 900, 1400
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Max's Game") #Set name of window 
#def game vars
vec = pygame.math.Vector2
ACCELERATION = .8
FRICTION = -0.1
FPS = 60
blocksize = (30,30)
platformsize = (WIDTH-1200,30)
Time = pygame.time.Clock()
#map images
image_map1=pygame.image.load("Fgamev2\\Mappics\\1.jpg")

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)
#https://coderslegacy.com/python/pygame-platformer-game-development/, largely based off this game, but modifed to be a goal platfomer insted of a vert platformer

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
        self.acc = vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACCELERATION
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACCELERATION
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0
            
        self.rect.midbottom = self.pos 
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
           self.vel.y = -10
    def cancel_jump(self):
        if self.jump:
            if self.vel.y < -3:
                self.vel.y = -3
    def update(self):
        hits = pygame.sprite.spritecollide(PLR ,platforms, False)
        if PLR.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((random.choice(randclr)))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),random.randint(90, HEIGHT-40)))
    def movement(self):
        pass
def plat_gen():
    while len(platforms) < 7 :
        width = random.randrange(50,100)
        p  = platform()             
        p.rect.center = (random.randrange(0, WIDTH - width),random.randrange(-50, 0))
        platforms.add(p)
        Bacisent.add(p)
class Finline(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 0))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center= (WIDTH,77))
    def movement(self):
        pass
PLR = playermodel()
PLAT = platform()
FIN = Finline()
#group inits
Bacisent = pygame.sprite.Group()
Bacisent.add(PLAT)
Bacisent.add(PLR)
Bacisent.add(FIN)

PLAT.surf = pygame.Surface((WIDTH, 20))
PLAT.surf.fill((183,124,95))
PLAT.rect = PLAT.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

platforms = pygame.sprite.Group()
platforms.add(PLAT)
platforms.add(FIN)
#game loop
game1 = True
while game1:
    for x in range(5):
        PLAT = platform()
        platforms.add(PLAT)
        Bacisent.add(PLAT)
    game2 = True
    while game2 == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    PLR.jump()
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_SPACE:
                    PLR.cancel_jump() 
            keyBoardKey=pygame.key.get_pressed()
            if keyBoardKey[pygame.K_e]:
                game2 = False
        SCREEN.blit(image_map1,(0,0))
        for i in range(10):
            draw_dashed_line(SCREEN, BLACK, (0,i*4+40), (WIDTH+40, i*4+40), dash_length=40)
            draw_dashed_line(SCREEN, WHITE, (-40,i*4+40), (WIDTH+40, i*4+40), dash_length=40)
            draw_dashed_line(SCREEN, BLACK, (0,i*4+39), (WIDTH+40, i*4+39), dash_length=40)
            draw_dashed_line(SCREEN, WHITE, (-40,i*4+39), (WIDTH+20, i*4+39), dash_length=40)
                    
            draw_dashed_line(SCREEN, WHITE, (0,i*4+38), (WIDTH+40, i*4+38), dash_length=40)
            draw_dashed_line(SCREEN, BLACK, (-40,i*4+38), (WIDTH+40, i*4+38), dash_length=40)
            draw_dashed_line(SCREEN, WHITE, (0,i*4+37), (WIDTH+40, i*4+37), dash_length=40)
            draw_dashed_line(SCREEN, BLACK, (-40,i*4+37), (WIDTH+40, i*4+37), dash_length=40)
            print(i*4+40), print(i*4+37)
        PLR.update()
        for entity in Bacisent: #Puts ents on to screen
            SCREEN.blit(entity.surf, entity.rect)
            entity.movement()
        pygame.display.update()
        Time.tick(FPS)