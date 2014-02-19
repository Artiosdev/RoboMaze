import sys, pygame, os, Buttons

from pygame.locals import *

pygame.init()

size=width,height=600,400 # the height and the width of the screen

screen= pygame.display.set_mode(size) # display the screen the  

menu=pygame.image.load('Concept_Art4.png') # load the image
menu=pygame.transform.scale(menu,(600,400)) # change the size of the image in terms of height and width

maze1=pygame.image.load('Concept_Art3.png') # Same as above
maze1=pygame.transform.scale(maze1,(1258,818))

playButton=Buttons.Button() # Set up an object Button 




while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # enable the game to quit
                sys.exit(0)

            elif event.type == MOUSEBUTTONDOWN: 
                if playButton.pressed(pygame.mouse.get_pos()): 
                    newSize=width,height=1258,818              # new size for the screen
                    screen= pygame.display.set_mode(newSize)   # set up a screen witht the new size
                    menu=pygame.transform.scale(menu,(0,0))    # resizing the menu screen so it disappear
                    screen.blit(menu,(0,0))                    # apply the changes with menu to the screen
                    pygame.display.flip()                      # display the changes to the menu
                    screen.blit(maze1,(0,0))                   # apply the changes with maze to the screen
                    pygame.display.flip()
                    pygame.display.update()                    # update the change to the sc 

        playButton.create_button(screen,(173,216,230),30,85,100,50,6,'Play',(0,0,0))
        screen.blit(menu,(0,0))
                    
        pygame.display.flip()
        pygame.display.update()
        
        

        
    except SystemExit as a:
        if a.code == 0:
            os._exit(0)

