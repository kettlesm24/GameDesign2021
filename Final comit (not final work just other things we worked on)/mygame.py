import pygame
import time
import sys
import os
import datetime
from pygame.draw import circle

from pygame.key import get_pressed 

pygame.init()
pygame.time.delay(100)
WIDTH = 800
HIGHT = 600
BLACK = [0,0,0]
WHITE = [255,255,255]
PURPLE = [200,4,200]
GREEN = [25,250,25]
RED = [255,0,0]
screen = pygame.display.set_mode((WIDTH,HIGHT))
screen.fill(BLACK)
pygame.display.set_caption("My Game")
pygame.display.update


#K_UP
#K_DOWN
#K_LEFT
#K_RIGHT

bg = pygame.image.load("images/stones.png")
some = pygame.image.load
check = True
rectx = 10
recty = 10
hbox, wbox = 20,20

rectx2 = 30
recty2 = 10
hbox2, wbox2 = 20,20

colorcircle = (RED)
cirx = 50
ciry = 10
rad = 30

while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    speed = 8
    keyBoardKey=pygame.key.get_pressed()
    if keyBoardKey[pygame.K_LEFT]:
        rectx -=speed
    if keyBoardKey[pygame.K_RIGHT]:
        rectx +=speed
    if keyBoardKey[pygame.K_UP]:
        recty -=speed
    if keyBoardKey[pygame.K_DOWN]:
        recty +=speed
    if keyBoardKey[pygame.K_j]:
        rectx2 -=speed
    if keyBoardKey[pygame.K_l]:
        rectx2 +=speed
    if keyBoardKey[pygame.K_i]:
        recty2 -=speed
    if keyBoardKey[pygame.K_k]:
        recty2 +=speed
    if keyBoardKey[pygame.K_a]:
        cirx -=speed
    if keyBoardKey[pygame.K_d]:
        cirx +=speed
    if keyBoardKey[pygame.K_w]:
        ciry -=speed
    if keyBoardKey[pygame.K_s]:
        ciry +=speed
    if keyBoardKey[pygame.K_z]:
        rad +=speed
    if keyBoardKey[pygame.K_x]:
        rad -=speed
    if keyBoardKey[pygame.K_n]:
        hbox -=speed
        wbox -=speed
    if keyBoardKey[pygame.K_m]:
        hbox +=speed
        wbox +=speed
    if rectx < 0:rectx=0
    if recty < 0:recty=0
    if rectx > WIDTH-wbox:rectx =WIDTH-wbox
    if recty > HIGHT-hbox:recty =HIGHT-hbox
    if rad < 0: rad = 1
    if cirx < 0:cirx=0
    if ciry < 0:ciry=0
    if rad > WIDTH-cirx: rad = WIDTH-cirx 
    if rad > HIGHT-ciry: rad = HIGHT-ciry 
    screen.fill(BLACK)
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,(RED),(rectx2,recty2,hbox2,wbox2))
    pygame.draw.rect(screen,(WHITE),(rectx,recty,hbox,wbox))
    pygame.draw.circle(screen, (WHITE), (cirx,ciry), rad,2)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()

