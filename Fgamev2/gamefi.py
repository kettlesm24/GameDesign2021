#Max Kettles Final proj 6/22
import os, sys, time, pygame, random, math, numpy
os.system('cls')
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
#RPG colors 
clr1 = (48, 52, 109)
clr2 = (78, 74, 78)
clr3 = (133, 76, 48)
clr4 = (52, 101, 36)
clr5 = (208, 70, 72)
clr6 = (117, 113, 97)
clr7 = (89, 125, 206)
clr8 = (210, 125, 44)
clr9 = (133, 149, 161)
clr10 = (109, 170, 44)
clr11 = (210, 170, 153)
clr12 = (109, 194, 202)
clr13 = (218, 212, 94)
clr14 = (222, 238, 214)
clrext = (210,55,41)
clr_mor = (255,170,150)
clr_mid = (67,162,255)
clr_night = (15,7,47)
#backgroundimg
image_moring=pygame.image.load("Fgamev2\\Menupics\\1.jpg")
image_day=pygame.image.load("Fgamev2\\Menupics\\2.png")
image_night=pygame.image.load("Fgamev2\\Menupics\\3.jpg")
image_map1=pygame.image.load("Fgamev2\\Mappics\\1.jpg")
#def screen vars 
HEIGHT, WIDTH = 900, 1400
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Max's Game") #Set name of window 
#def game vars
vec = pygame.math.Vector2
vec = pygame.math.Vector2
ACCELERATION = .8
FRICTION = -0.1
FPS = 60
blocksize = (30,30)
platformsize = (WIDTH-1200,30)
Time = pygame.time.Clock()
Time = pygame.time.Clock()
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size 
LetterFont=pygame.font.SysFont("comicsans",40)
Wbox = 160
Hbox = 90
timeday = ""
first_pos = WIDTH/4-Wbox
middle_pos = WIDTH/2-Wbox
last_pos = WIDTH-WIDTH/4-Wbox
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
    def update2(self):
        hits = pygame.sprite.spritecollide(PLR ,finlineg, True)
        if hits:
                varfin=True
                return varfin
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
        self.surf = pygame.Surface((WIDTH*2, 1))
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

finlineg = pygame.sprite.Group()
finlineg.add(FIN)

def timecheck(timeday):
    test = True
    while test:
        message="What time is it?"
        SCREEN.fill(WHITE)
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr13, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #Moring
        rect1=pygame.Rect(first_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr_mor, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render("Sunrise", 1, BLACK)
        SCREEN.blit(text, (first_pos+50,rect1.y+60))
       
        #Mid day
        rect2=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr_mid, rect2, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect2, width=10)
        text = TitleFont.render("Mid Day", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect2.y+60))

        #Night
        rect3=pygame.Rect(last_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr_night, rect3, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect3, width=10)
        text = TitleFont.render("Night", 1, WHITE)
        SCREEN.blit(text, (last_pos+80,rect2.y+60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    timeday = 1
                    Menu(timeday)
                if rect2.collidepoint((mx,my)):
                    timeday = 2
                    Menu(timeday)
                if rect3.collidepoint((mx,my)):
                    timeday = 3
                    Menu(timeday)
        pygame.display.update() 
def Menu(timeday):
    testmenu=True
    while testmenu:
        message="Which option do you chose?"
        if timeday == 1:
            image_time = image_moring
        if timeday == 2:
            image_time = image_day
        if timeday == 3:
            image_time = image_night
        SCREEN.blit(image_time,(0,-50))
        timeday=0
        #Print message
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr13, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #option1
        rect1=pygame.Rect(first_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render("Play", 1, BLACK)
        SCREEN.blit(text, (first_pos+100,rect1.y+60))
       
        #option2
        rect2=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect2, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect2, width=10)
        text = TitleFont.render("Levels", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect2.y+60))

        #option3
        rect3=pygame.Rect(last_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr9, rect3, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect3, width=10)
        text = TitleFont.render("Char Select", 1, BLACK)
        SCREEN.blit(text, (last_pos+20,rect2.y+60))
        #option4
        rect4=pygame.Rect(first_pos, 550, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr8, rect4, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect4, width=10)
        text = TitleFont.render("Map Select", 1, BLACK)
        SCREEN.blit(text, (first_pos+20,rect4.y+60))
        #option5
        rect5=pygame.Rect(middle_pos, 550, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr12, rect5, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect5, width=10)
        text = TitleFont.render("Leaderboard", 1, BLACK)
        SCREEN.blit(text, (middle_pos+10,rect5.y+60))
        #exit
        rect6=pygame.Rect(last_pos, 550, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clrext, rect6, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect6, width=10)
        text = TitleFont.render("Exit", 1, BLACK)
        SCREEN.blit(text, (last_pos+100 , rect6.y+60))
       
        #Check collide Point and rectangle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    maingame()
                if rect2.collidepoint((mx,my)):
                    Levels()
                if rect3.collidepoint((mx,my)):
                    Char_Select()
                if rect4.collidepoint((mx,my)):
                    Map_Select()
                if rect5.collidepoint((mx,my)):
                    Leaderboard()
                if rect6.collidepoint((mx,my)):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()  
def maingame():
    testgame = True
    while testgame:
        SCREEN.fill(WHITE)
        message = "Which option do you chose?"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #exit option
        rect1=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render(" Start", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect1.y+60))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                
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
                        PLR.update()
                        varfin = PLR.update2()
                        for entity in Bacisent:
                            SCREEN.blit(entity.surf, entity.rect)
                            entity.movement()
                        pygame.display.update()
                        Time.tick(FPS)
                        if varfin==True:
                            game1=False
                            game2=False
                            break
def Levels():
    test = True
    while test:
        SCREEN.fill(WHITE)
        message = "Levels Func"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #exit option
        rect1=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render(" Menu", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect1.y+60))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    test = False
                    break
def Char_Select():
    test = True
    while test:
        SCREEN.fill(WHITE)
        message = "Char_Select"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #exit option
        rect1=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render(" Menu", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect1.y+60))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    test = False
                    break
def Map_Select():

    test = True
    while test:
        SCREEN.fill(WHITE)
        message = "Map_Select"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #exit option
        rect1=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render(" Menu", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect1.y+60))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    test = False
                    break
def Leaderboard():
    test = True
    while test:
        SCREEN.fill(WHITE)
        message = "Leaderboard"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #exit option
        rect1=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render(" Menu", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect1.y+60))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1.collidepoint((mx,my)):
                    test = False
                    break
while True:
    timecheck(timeday)
    Menu(timeday)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  