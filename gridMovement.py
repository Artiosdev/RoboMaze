import pygame ,sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((500,500))
pygame.display.set_caption("Testing")

width = 50 # squarewidth = width of maze image / number of squares
height = 50 

gridObj = pygame.image.load("grid.jpg")
spriteObj = pygame.image.load("sprite.png").convert_alpha()
white = pygame.Color(255,255,255)

playerposition = [5,5]  # X,Y

direction = 0;

moveX = 0
moveY = 0
soundObj = pygame.mixer.Sound("atari.wav")
soundObj2 = pygame.mixer.Sound("computer_move.wav")
while True:
    #windowSurfaceObj.fill(white)

    windowSurfaceObj.blit(gridObj,(0,0))
    windowSurfaceObj.blit(spriteObj,(playerposition[0]*height,playerposition[1]*width))



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if (event.type==pygame.KEYDOWN): 
            if direction==360:
                direction=0
            if (event.key==pygame.K_LEFT): 
                spriteObj=pygame.transform.rotate(spriteObj,90)
                if direction==0:
                    direction=360
                direction-=90
                soundObj2.play()
            elif (event.key==pygame.K_RIGHT): 
                spriteObj=pygame.transform.rotate(spriteObj,-90)
                direction+=90
                soundObj2.play()
            elif (event.key==pygame.K_UP):
                if direction == 270:
                    if playerposition[1]==0:
                        moveY=0
                        soundObj.play()
                    else: 
                        moveY = -1
                        soundObj2.play()
                elif direction == 90:
                     if playerposition[1]==9:
                        moveY=0
                        soundObj.play()
                     else:
                        moveY = 1
                        soundObj2.play()
                elif direction == 180:
                     if playerposition[0]==0:
                        moveX=0
                        soundObj.play()
                     else: 
                        moveX = -1
                        soundObj2.play()
                elif direction == 0:
                     if playerposition[0]==9:
                        moveX=0
                        soundObj.play()
                     else: 
                        moveX = 1
                        soundObj2.play()

  
        if (event.type==pygame.KEYUP): 
  
            if (event.key==pygame.K_LEFT): 
  
                moveX= 0
  
            elif (event.key==pygame.K_RIGHT): 
  
                moveX= 0
  
            elif (event.key==pygame.K_UP): 
  
                moveY= 0
  
            elif (event.key==pygame.K_DOWN): 
  
                moveY= 0
            
    playerposition[0] += moveX
    playerposition[1] += moveY

    moveX = 0
    moveY = 0

    pygame.display.update()
    fpsClock.tick(30)
