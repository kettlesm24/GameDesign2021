#Max Kettles Final proj 6/22

import os, sys, time, pygame, random, math
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
image_moring=pygame.image.load("Fgamev1\\Menupics\\1.jpg")
image_day=pygame.image.load("Fgamev1\\Menupics\\2.png")
image_night=pygame.image.load("Fgamev1\\Menupics\\3.jpg")
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
TitleFont= pygame.font.SysFont("comicsans", 70)  #set the type of font and the size 
LetterFont=pygame.font.SysFont("comicsans",40)
Wbox = 160
Hbox = 90
timeday = ""
first_pos = WIDTH/4-Wbox
middle_pos = WIDTH/2-Wbox
last_pos = WIDTH-WIDTH/4-Wbox
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
                    print("work1")
                    timeday = 1
                    Menu(timeday)
                if rect2.collidepoint((mx,my)):
                    print("work2")
                    timeday = 2
                    Menu(timeday)
                if rect3.collidepoint((mx,my)):
                    print("work3")
                    timeday = 3
                    Menu(timeday)
        pygame.display.update() 
def Menu(timeday):
    test=True
    while test:
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
    test = True
    while test:
        SCREEN.fill(WHITE)
        message = "Play Func"
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
                    timecheck(timeday)
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
                    timecheck(timeday)
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
                    timecheck(timeday)
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
                    timecheck(timeday)
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
                    timecheck(timeday)
while True:
    timecheck(timeday)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 