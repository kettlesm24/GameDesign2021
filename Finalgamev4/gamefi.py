#Max Kettles Final proj 6/22
#For the functions outside of the main game I am using text boxes and then mouse clicks to activate and change diffrent parts of the main game
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
randclr1=[(207,206,192),(163,163,161),(205,205,205)]#these 3 lists somewhat match the color of each map and when you chose the map is also selects the color
randclr2=[(56, 112, 80),(8, 88, 72),(16, 64, 40),(168, 200, 208)]
randclr3=[(74, 39, 98),(63, 79, 80),(215, 214, 234),(79, 180, 251)]
#RPG colors, just clrs I thought sorta matched the RPG colors
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
#backgroundimg, these images chnage depending on what the player selects for their time
#https://wallpaperaccess.com/pixel-art-clouds
image_moring=pygame.image.load("Finalgamev4\\Menupics\\1.jpg")
image_day=pygame.image.load("Finalgamev4\\Menupics\\2.png")
image_night=pygame.image.load("Finalgamev4\\Menupics\\3.jpg")
#https://www.artstation.com/artwork/ddBBe, these images chnage depending on what the player has set in the settings file
image_map1=pygame.image.load("Finalgamev4\\Mappics\\1.jpg")
image_map2=pygame.image.load("Finalgamev4\\Mappics\\2.png")
image_map3=pygame.image.load("Finalgamev4\\Mappics\\3.png")
#def screen vars 
HEIGHT, WIDTH = 900, 1400
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Max's Game") #Set name of window 
#def game vars
vec = pygame.math.Vector2 # lets the spries know 2d
ACCELERATION = .8 #some vars that were needed for the sprites
FRICTION = -0.1
FPS = 60
blocksize = (30,30) 
platformsize = (WIDTH-1200,30)
Time = pygame.time.Clock()#needed to make the jump and move work well
TitleFont= pygame.font.SysFont("georgia", 52)  #set the type of font and the size 
LetterFont=pygame.font.SysFont("georgia",30)
Wbox = 160
Hbox = 90
timeday = ""
first_pos = WIDTH/4-Wbox
middle_pos = WIDTH/2-Wbox
last_pos = WIDTH-WIDTH/4-Wbox
#https://codereview.stackexchange.com/questions/70143/drawing-a-dashed-line-with-pygame, I used this to make the finish line 
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
#https://coderslegacy.com/python/pygame-platformer-game-development/, the whole game largely based off this game, but modifed to be a goal platfomer insted of a vert platformer among other changes

#def player and all actions of player sprite such as all movement and finishing func
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
            if difficulty ==3:
                print(Name)
                print(score)
                file=open("Finalgamev4\scoref.txt","a")
                file.write(str(score)+"_"+Name+"                                                                                                                                                     \n")
                file.close()
            varfin=True
            return varfin
class platform(pygame.sprite.Sprite):#def basic platform and where to place it, its random so each time I call it it gets put in a diffrent place
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill(WHITE)
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
class Finline(pygame.sprite.Sprite): #def finline mainly for coliding with player then end the game
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
#group create so I call call them all at once
Bacisent = pygame.sprite.Group()
platforms = pygame.sprite.Group()
finlineg = pygame.sprite.Group()

def timecheck(timeday):# start of my main func, THis one asks for initals, then for time, out of 3 options, then goes onto main menu loop
    message="Input your initials in the Terminal"
    SCREEN.fill(WHITE)
    rect0=pygame.Rect(middle_pos-300,300,920,Hbox*2)#all of my rect prints and clicks are all pretty much the same, I first define the rect, draw the inside and border of the rect, then layer the text on top of it 
    #I then use the same rect to see when it gets clicked on 
    pygame.draw.rect(SCREEN, clr6, rect0, width=0)
    pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
    text = TitleFont.render(message, 1, BLACK)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 360))
    pygame.display.update() 
    global Name
    Name=input("What are your initials? ")#records name of player in terminal to be used later when recording score
    test = True
    while test:#first option loop, ends when a time is selected, then player is taken to menu
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
                    timeday = 1#takes var timeday to menu where it desides what background to use
                    Menu(timeday)#goes to menu
                if rect2.collidepoint((mx,my)):
                    timeday = 2
                    Menu(timeday)
                if rect3.collidepoint((mx,my)):
                    timeday = 3
                    Menu(timeday)
        pygame.display.update() 
def Menu(timeday):#Main menu loop
    message="Which option do you chose?"
    global image_time
    if timeday == 1:#processes timeday and defines the background
        image_time = image_moring
    if timeday == 2:
        image_time = image_day
    if timeday == 3:
        image_time = image_night
    testmenu=True
    while testmenu:
        SCREEN.blit(image_time,(0,-50))
        timeday=0
        #Print message, more of the same rect and click functions
        rect10=pygame.Rect(middle_pos-300,50,920,Hbox*2)
        pygame.draw.rect(SCREEN, clr14, rect10, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect10, width=10)
        text = TitleFont.render("Pixel Climbers", 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 120))
        #Print message
        rect0=pygame.Rect(middle_pos-200,250,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 300))
        #option1
        rect1=pygame.Rect(first_pos, 450, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr13, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render("Play", 1, BLACK)
        SCREEN.blit(text, (first_pos+100,rect1.y+60))
       
        #option2
        rect2=pygame.Rect(middle_pos, 450, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect2, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect2, width=10)
        text = TitleFont.render("Levels", 1, BLACK)
        SCREEN.blit(text, (middle_pos+80,rect2.y+60))

        #option3
        rect3=pygame.Rect(last_pos, 450, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr9, rect3, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect3, width=10)
        text = TitleFont.render("Tutorial", 1, BLACK)
        SCREEN.blit(text, (last_pos+70,rect2.y+60))
        #option4
        rect4=pygame.Rect(first_pos, 650, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr8, rect4, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect4, width=10)
        text = TitleFont.render("Map Select", 1, BLACK)
        SCREEN.blit(text, (first_pos+20,rect4.y+60))
        #option5
        rect5=pygame.Rect(middle_pos, 650, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr12, rect5, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect5, width=10)
        text = TitleFont.render("Leaderboard", 1, BLACK)
        SCREEN.blit(text, (middle_pos+10,rect5.y+60))
        #exit
        rect6=pygame.Rect(last_pos, 650, Wbox*2,Hbox*2)
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
                if rect1.collidepoint((mx,my)):#all of the options in the menu
                    maingame(PLAT,PLR,FIN,Bacisent,platforms,finlineg)
                if rect2.collidepoint((mx,my)):
                    Levels()
                if rect3.collidepoint((mx,my)):
                    Tutorial()
                if rect4.collidepoint((mx,my)):
                    Map_Select()
                if rect5.collidepoint((mx,my)):
                    Leaderboard()
                if rect6.collidepoint((mx,my)):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()  
def maingame(PLAT,PLR,FIN,Bacisent,platforms,finlineg):#Main game func, the game is a climbing game using the class system and key presses to function
    testgame = True
    while testgame:
        SCREEN.blit(image_time,(0,-50))
        #Title message
        message = "Which option do you chose?"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #Start option
        rect1=pygame.Rect(middle_pos-150, 350, Wbox*2+300,Hbox*2)
        pygame.draw.rect(SCREEN, clr10, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render(" Start", 1, BLACK)
        SCREEN.blit(text, (middle_pos+70,rect1.y+60))
        #exit option
        rect2=pygame.Rect(middle_pos-150, 550, Wbox*2+300,Hbox*2)
        pygame.draw.rect(SCREEN, clrext, rect2, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect2, width=10)
        text = TitleFont.render("Exit", 1, BLACK)
        SCREEN.blit(text, (middle_pos+100 , rect2.y+60))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:

                mx,my= pygame.mouse.get_pos()
                if rect2.collidepoint((mx,my)):
                    testgame=False
                    break
                if rect1.collidepoint((mx,my)):#Starts main game, I first look at both settings files for what background,colors, and how many platforms to spawn in
                    file = open("Finalgamev4\settings.txt","r")#Basic read file func
                    readsettings = file.readlines()
                    setting = (str(readsettings[0]))
                    if setting =="1":
                        mapset = image_map1
                        randclr = randclr1
                    if setting =="2":
                        mapset = image_map2
                        randclr = randclr2
                    if setting =="3":
                        mapset = image_map3
                        randclr = randclr3
                    file.close()
                    file = open("Finalgamev4\difficulty.txt","r")
                    readsettings = file.readlines()
                    setting = (str(readsettings[0]))
                    global difficulty
                    if setting =="1":
                        difficulty=6
                    if setting =="2":
                        difficulty=4
                    if setting =="3":
                        difficulty=2                        
                    file.close()
                    global score
                    score = -1#Funcs below this make sure the game is reset to a blank slate and none of the platforms are left over from the game that was previously played
                    Bacisent.empty()
                    platforms.empty()
                    finlineg.empty()
                    Bacisent.add(PLAT)
                    Bacisent.add(PLR)
                    Bacisent.add(FIN)
                    PLAT.surf = pygame.Surface((WIDTH, 20))#these lines define the bottom platform so the player does not fall through
                    PLAT.surf.fill(random.choice(randclr))
                    PLAT.rect = PLAT.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
                    platforms.add(PLAT)
                    platforms.add(FIN)
                    finlineg.add(FIN)
                    PLR.pos = vec((150, HEIGHT-30))#resets player to bottom of map 
                    game1 = True #plays everytime the player presses E 
                    for entity in Bacisent:
                        SCREEN.blit(entity.surf, entity.rect)
                        entity.movement()
                    for x in range(8):#scores start at 10 becuase you cant start with less than 10 platforms
                        PLAT = platform()
                        PLAT.surf.fill(random.choice(randclr))
                        platforms.add(PLAT)
                        Bacisent.add(PLAT)
                    while game1:
                        for x in range(difficulty):
                            PLAT = platform()
                            PLAT.surf.fill(random.choice(randclr))
                            platforms.add(PLAT)
                            Bacisent.add(PLAT)
                        score = score + 1 
                        game2 = True #loops platforms and keystokes
                        while game2 :
                            varfin=False
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:    
                                    if event.key == pygame.K_SPACE:#calls jump from player
                                        PLR.jump()
                                if event.type == pygame.KEYUP:    
                                    if event.key == pygame.K_SPACE:#this is the smaller jump it you just tap instead pf holding space
                                        PLR.cancel_jump() 
                                keyBoardKey=pygame.key.get_pressed()
                                if keyBoardKey[pygame.K_e]:#spanws in new platforms and adds to score
                                    game2 = False
                            SCREEN.blit(mapset,(0,0))
                            for i in range(10):#draws dotted lines and forms finish line
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
                            for entity in Bacisent:#Loads all of the ents into the screen, also loads left and right movement 
                                SCREEN.blit(entity.surf, entity.rect)
                                entity.movement()
                            pygame.display.update()
                            Time.tick(FPS)
                            if varfin==True:#Ends game once player hits the top of the screen
                                game1=False
                                game2=False
                                break
def Levels():#this function detrimens the map and colors in the levels buy using the same rect/click but also storeing the setting in sepreate file
    test = True
    while test:
        SCREEN.blit(image_time,(0,-50))
        message = "Level Select"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #1st 
        rect1=pygame.Rect(first_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr6, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render("Easy", 1, BLACK)
        SCREEN.blit(text, (first_pos+100,rect1.y+60))
        #2nd
        rect2=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr7, rect2, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect2, width=10)
        text = TitleFont.render("Medium", 1, BLACK)
        SCREEN.blit(text, (middle_pos+60,rect2.y+60))
        #3rd
        rect3=pygame.Rect(last_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr3, rect3, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect3, width=10)
        text = TitleFont.render("Hard", 1, BLACK)
        SCREEN.blit(text, (last_pos+100,rect2.y+60))

        rect4=pygame.Rect(middle_pos-150, 550, Wbox*2+300,Hbox*2)
        pygame.draw.rect(SCREEN, clrext, rect4, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect4, width=10)
        text = TitleFont.render("Exit", 1, BLACK)
        SCREEN.blit(text, (middle_pos+100 , rect4.y+60))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect4.collidepoint((mx,my)):
                    test = False
                    break
                if rect1.collidepoint((mx,my)):#for each choice I write either 1 2 or 3 in a seprate file
                    file_w=open("Finalgamev4\difficulty.txt","w")
                    file_w.write(str("1"))
                    file_w.close()
                    test = False
                    break
                if rect2.collidepoint((mx,my)):
                    file_w=open("Finalgamev4\difficulty.txt","w")
                    file_w.write(str("2"))
                    file_w.close()
                    test = False
                    break
                if rect3.collidepoint((mx,my)):
                    file_w=open("Finalgamev4\difficulty.txt","w")
                    file_w.write(str("3"))
                    file_w.close()
                    test = False
                    break
def Tutorial():#a simple rect and click where I just expanded one of the rects and put a lot of text in the rect
    test = True
    while test:
        SCREEN.blit(image_time,(0,-50))
        message = "Tutorial"
        rect0=pygame.Rect(middle_pos-200,60,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 130))
        #exit option
        rect1=pygame.Rect(100, 270, WIDTH-200,HEIGHT-450)
        pygame.draw.rect(SCREEN, clr10, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = LetterFont.render("The goal of Pixel Climbers is to reach the top of the Moutian(aka the screen)", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+20))
        text = LetterFont.render("The player achives the goal by jumping to and from the platforms on the Moutian", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+60))
        text = LetterFont.render("At the start the player probaly cant get all the way up because of the lack of platforms", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+100))
        text = LetterFont.render("In order for the player to reach the top he must spawn in more platforms by pressing E", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+140))
        text = LetterFont.render("With each press of E your score goes up by 1, the lower your score is the better", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+180))
        text = LetterFont.render("To keep the scores balanced, scores are only recorded for the hard level setting", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+220))
        text = LetterFont.render("You can change the look and difficulty of the game with the Map Select and Levels options", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+260))
        text = LetterFont.render("Controls:", 1, BLACK)
        SCREEN.blit(text, (middle_pos+50,rect1.y+310))
        text = LetterFont.render("Left arrow = move left, Right arrow = move right, Space bar = jump, E = spawn platform", 1, BLACK)
        SCREEN.blit(text, (first_pos-70,rect1.y+360))
        #exit box
        rect4=pygame.Rect(middle_pos-10, 750, Wbox*2,Hbox*2-70)
        pygame.draw.rect(SCREEN, clrext, rect4, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect4, width=10)
        text = TitleFont.render("Exit", 1, BLACK)
        SCREEN.blit(text, (middle_pos+100 , rect4.y+20))        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect4.collidepoint((mx,my)):
                    test = False
                    break

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
def Map_Select():#very similar to the previous function for selecting difficulty
    test = True
    while test:
        SCREEN.blit(image_time,(0,-50))
        message = "Map Select"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 200))
        #1st 
        rect1=pygame.Rect(first_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr6, rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = LetterFont.render("Tronear Volcano", 1, BLACK)
        SCREEN.blit(text, (first_pos+40,rect1.y+60))
        #2nd
        rect2=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr7, rect2, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect2, width=10)
        text = LetterFont.render("Applegue Summit", 1, BLACK)
        SCREEN.blit(text, (middle_pos+40,rect2.y+60))
        #3rd
        rect3=pygame.Rect(last_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, clr3, rect3, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect3, width=10)
        text = LetterFont.render("Lincaster Highlands", 1, BLACK)
        SCREEN.blit(text, (last_pos+30,rect2.y+60))

        rect4=pygame.Rect(middle_pos-150, 550, Wbox*2+300,Hbox*2)
        pygame.draw.rect(SCREEN, clrext, rect4, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect4, width=10)
        text = TitleFont.render("Exit", 1, BLACK)
        SCREEN.blit(text, (middle_pos+100 , rect4.y+60))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect4.collidepoint((mx,my)):
                    test = False
                    break
                if rect1.collidepoint((mx,my)):
                    file=open("Finalgamev4\settings.txt","w")
                    file.write(str("1"))
                    file.close()
                    test = False
                    break
                if rect2.collidepoint((mx,my)):
                    file=open("Finalgamev4\settings.txt","w")
                    file.write(str("2"))
                    file.close()
                    test = False
                    break
                if rect3.collidepoint((mx,my)):
                    file=open("Finalgamev4\settings.txt","w")
                    file.write(str("3"))
                    file.close()
                    test = False
                    break
def Leaderboard():
    #I open the leaderboard file right here, then call top 3 and sort them and define them using the score file from before
    TOPSCORES=[]
    file = open("Finalgamev4\scoref.txt","r")
    readscores = file.readlines()
    sortedscores = sorted(readscores)
    for line in range(4):
        scoreprint = (str(sortedscores[line]))
        TOPSCORES.append(scoreprint)
    file.close()
    test = True
    while test:
        SCREEN.blit(image_time,(0,-50))
        message = "Leaderboard"
        rect0=pygame.Rect(middle_pos-200,130,720,Hbox*2)
        pygame.draw.rect(SCREEN, clr11, rect0, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect0, width=10)
        text = TitleFont.render(message, 1, BLACK)
        SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 150))
        text2 = TitleFont.render("scores start at 10", 1, BLACK)#scores start at 10 becuae there are 10 platforms
        SCREEN.blit(text2, (WIDTH/2 - text2.get_width()/2, 230))
        #1st 
        rect1=pygame.Rect(first_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, (255,215,0), rect1, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect1, width=10)
        text = TitleFont.render("1."+"_"+TOPSCORES[1], 1, BLACK)
        SCREEN.blit(text, (first_pos+40,rect1.y+60))
        #2nd
        rect2=pygame.Rect(middle_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, (192,192,192), rect2, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect2, width=10)
        text = TitleFont.render("2."+"_"+TOPSCORES[2], 1, BLACK)
        SCREEN.blit(text, (middle_pos+40,rect2.y+60))
        #3rd
        rect3=pygame.Rect(last_pos, 350, Wbox*2,Hbox*2)
        pygame.draw.rect(SCREEN, (176,141,87), rect3, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect3, width=10)
        text = TitleFont.render("3."+"_"+TOPSCORES[3], 1, BLACK)
        SCREEN.blit(text, (last_pos+40,rect2.y+60))

        rect4=pygame.Rect(middle_pos-150, 550, Wbox*2+300,Hbox*2)
        pygame.draw.rect(SCREEN, clrext, rect4, width=0)
        pygame.draw.rect(SCREEN, BLACK, rect4, width=10)
        text = TitleFont.render("Exit", 1, BLACK)
        SCREEN.blit(text, (middle_pos+100 , rect4.y+60))


        pygame.display.update()
    #I will close the file here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect4.collidepoint((mx,my)):
                    test = False
                    break
while True:#Simple main game loop where call main functions and also have the quit func
    timecheck(timeday)
    Menu(timeday)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  