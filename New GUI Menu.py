import pygame, Buttons, robot, grid
#from pygame.locals import*
#from sys import exit




class PygView():

  
    def __init__(self,height, width, fps):
        """Initialize pygame, window, background, font,...
"""
        pygame.init() # define the pygame interface
        pygame.display.set_caption("RoboGuide - Press ESC to quit")
        self._infoObj = pygame.display.Info()
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN) #initialise the screen
        self._instructionScreen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN)
        self._mazeScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN)
        self._dictionaryScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN)
        self._helpScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN)
        self._optionScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN)
        self._menu = 0
        self._maze= 0
        self._instructions=0
        self._clock = pygame.time.Clock()
        self._fps = fps #Frames per second
        self._playtime = 0.0
        self._font = pygame.font.SysFont('mono', self._height // 30, bold=True) #set the font for the text
        self._playButton=Buttons.Button() #create an object of Button
        self._InstructButton=Buttons.Button()
        self._OptionButton=Buttons.Button()
        self._DictionaryButton=Buttons.Button()
        self._HelpButton=Buttons.Button()
        self._RunButton=Buttons.Button()
        self._backButton=Buttons.Button()
        self._map=0
        self._fpsClock = pygame.time.Clock()
        self._spriteObj = pygame.image.load("sprite.png").convert_alpha()

        self._Sprite1Button=Buttons.Button()
        self._Sprite2Button=Buttons.Button()
        self._Sprite3Button=Buttons.Button()       
        self._Sprite4Button=Buttons.Button()
        self._SoundButton=Buttons.Button()

        self._tempSprite = "Sprite 1"          #initialise the temporary sprite to be the computer
        self._soundOn=True

        self._soundObj = pygame.mixer.Sound("atari.wav")
        self._soundObj2 = pygame.mixer.Sound("computer_move.wav")
        self._gamemode = False
        self._menuMode = True

        self._robot1 = robot.spriteMovement(1,1)
        self._playerPosition = self._robot1.getPosition()

        self._level1 = grid.Grid(12,11)

    def moveForward(self):
        newplayerposition = self._robot1.CheckCollisions()
        if (self._level1.checkWall(newplayerposition[0],newplayerposition[1]) == True):
            self._soundObj.play()
            return True
        else:
            self._robot1.moveForward()
            if self._soundOn==True:
                self._soundObj2.play()     #if sound is on then play the sound
            else:
                self._soundObj2.stop()     #stop playback when sound is not on
            self._playerposition = self._robot1.getPosition()
            return False
        #if (level1.checkQuestion(newplayerposition[0],newplayerposition[1]) == True):
            ##Activate Question code
        #if (level1.checkEndpoint(newplayerposition[0],newplayerposition[1]) == True):
            ##Activate end code

    def rotateRight(self,spriteObj):
            self._robot1.rotateRight()
            spriteObj = pygame.transform.rotate(self._spriteObj,-90)
            return spriteObj

    def rotateLeft(self,spriteObj):
        self._robot1.rotateLeft()
        spriteObj = pygame.transform.rotate(self._spriteObj,90)
        return spriteObj

    def repeatedMove(self,direction,num):
            if direction == "forward":
                for n in range(1,num) :
                    moveForward();
            elif n == "right":
                for n in range(1,num):
                    rotateRight();
            elif direction == "left":
                for n in range(1,num):
                    rotateLeft();
    def repeatUntilCollision():
        collision = self.moveForward()
        while collision == False:
            collision = self.moveForward()
            

    def run(self):
        """The mainloop
"""
        running = True
        

        PygView.SetUpButtonMain(self)
        PygView.SetUpImage(self)
        
        while running:

            self._playerPosition = self._robot1.getPosition()
            



            if(self._menuMode == True):
                self._screen.blit(self._menu, (0, 0))

        
            
            if(self._gamemode == True):
                self._screen.blit(self._map,(0,0))
                self._screen.blit(self._spriteObj,(self._playerPosition[0]*(self._infoObj.current_w/20),self._playerPosition[1]*(self._infoObj.current_h/5)))
                ## The 22.5 and 10 values will change depending on the size of the map.
            
            for event in pygame.event.get():
               
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    elif (event.type==pygame.KEYDOWN):

                        if (event.key==pygame.K_LEFT):
                            self._spriteObj = self.rotateLeft(self._spriteObj)
                        elif (event.key==pygame.K_RIGHT):
                            self._spriteObj = self.rotateRight(self._spriteObj)
                        elif (event.key==pygame.K_UP):
                            self.moveForward()
                        elif (event.key==pygame.K_SPACE):
                            self.repeatUntilCollision()
                            
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self._backButton.pressed(pygame.mouse.get_pos()):
                        PygView.run(self)
                        
                    elif self._playButton.pressed(pygame.mouse.get_pos()):
                        #PygView.run(self)
                        PygView.SetUpButtonGamePlay(self)
                        self._width=569 # new width for the screen
                        self._height= 369 # new height for the screen
                        self._menu=pygame.transform.scale(self._menu,(0,0)) # resizing the menu screen so it disappear
                        self._mazeScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN)
                        pygame.display.flip() # display the changes to the menu
                        self.loadLevel(0)#the number will have to change using a counter
                        #pygame.display.flip()
                        #pygame.display.update() # update the change to the screen
                        self._gamemode = True
                        self._menuMode = False
                        self._level1.initialiseGrid()
                                                
                        
                        if self._DictionaryButton.pressed(pygame.mouse.get_pos()) :
                            self._width=569
                            self._height=369
                            self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN) # set up a screen with the new width and height
                            pygame.display.flip() # display the changes to the menu
                            self._screen.blit(self._screen,(0,0))
                            self._screen.fill((173,216,230))
                            pygame.display.flip()
                            pygame.display.update()


                        elif self._HelpButton.pressed(pygame.mouse.get_pos()) :
                            self._width=569
                            self._height=369
                            self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN) # set up a screen with the new width and height
                            pygame.display.flip() # display the changes to the menu
                            self._screen.blit(self._screen,(0,0))
                            self._screen.fill((173,216,230))
                            pygame.display.flip()
                            pygame.display.update()


                        elif self._RunButton.pressed(pygame.mouse.get_pos()) :
                            self._width=569
                            self._height=369
                            self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN) # set up a screen with the new width and height
                            pygame.display.flip() # display the changes to the menu
                            self._screen.blit(self._screen,(0,0))
                            self._screen.fill((173,216,230))
                            pygame.display.flip()
                            pygame.display.update()
                            
                        
                        
                            

                    elif self._InstructButton.pressed(pygame.mouse.get_pos()):
                        self._width=600
                        self._height=400
                        self._instructionScreen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN) # set up a screen with the new width and height
                        self._menu=pygame.transform.scale(self._menu,(0,0)) # resizing the menu screen so it disappear
                        self._screen.blit(self._menu,(0,0)) # apply the changes with menu to the screen
                        pygame.display.flip() # display the changes to the menu
                        self._screen.blit(self._instructionScreen,(0,0)) # apply the changes with maze to the screen
                        
                        self._screen.fill((173,216,230))
                        self.draw_text("Instructions", 300,0)
                        self.draw_text("Welcome to Robo-Guide. A game that will test your compatibility with the",20,40)
                        self.draw_text("Computer Science undergraduate course at Oxford Brookes. The game will",20,60)
                        self.draw_text("require you to safely navigate a robot through hazardous courses by ",20,80)
                        self.draw_text("typing in commands with your keyboard. The code you type into the game",20,100)
                        self.draw_text("will not require knowledge of any high level programming language. The ",20,120)
                        self.draw_text("code inputted will be very straightforward and the game will be able to",20,140)
                        self.draw_text("assist you.if you’re stuck when you press the help button during the ",20,160)
                        self.draw_text("game. The courses will have an end point that the user is supposed to ",20,180)
                        self.draw_text("reach, getting to this point faster will reward the player, however by",20,200)
                        self.draw_text("taking these shortcuts you may be required to answer questions related",20,220)
                        self.draw_text("to the computer science course. Incorrect answers will result in failure",20,240)
                        self.draw_text("in the level. Once the end point is reached a final question is asked,",20,260)
                        self.draw_text("a correct answer will allow the player to proceed to the next level",20,280)
                        self.draw_text("where the difficulty of the questions escalate.",20,300)
                        self._backButton.create_button(self._instructionScreen,(173,216,230),0,0,100,25,6,'Back',(0,0,0))
                        if self._backButton.pressed(pygame.mouse.get_pos()):
                            PygView.run(self)
                            
                        pygame.display.flip()
                        pygame.display.update()

                         

                    elif self._OptionButton.pressed(pygame.mouse.get_pos()) :
                        tempSprite=''
                        self._width=600
                        self._height=400
                        self._optionScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF|pygame.FULLSCREEN) # set up a screen with the new width and height
                        self._menu=pygame.transform.scale(self._menu,(0,0))                                  # resizing the menu screen so it disappear
                        self._screen.blit(self._menu,(0,0))                                                  # apply the changes with menu to the screen
                        pygame.display.flip()                                                                # display the changes to the menu
                        self._screen.blit(self._optionScreen,(0,0))
                        self._optionScreen.fill((173,216,230))
                        self.draw_text("Option", 250,0)

                        self.draw_text("Sprite choice:", 50,50)
                        self.draw_text("Sound on/off:", 50,100)
                        PygView.SetUpButtonOptions(self)
                        self._screen.blit(self._optionScreen,(0,0))    
                        pygame.display.flip()
                        pygame.display.update()

                        if self._backButton.pressed(pygame.mouse.get_pos()):
                            PygView.run(self)

                    elif self._Sprite1Button.pressed(pygame.mouse.get_pos()):
                        self._tempSprite="Computer"
                        PygView.changeSprite(self,self._tempSprite)

                    elif self._Sprite2Button.pressed(pygame.mouse.get_pos()):
                        self._tempSprite="Mushroom"
                        PygView.changeSprite(self,self._tempSprite)

                    elif self._Sprite3Button.pressed(pygame.mouse.get_pos()):            #alex edits for options no idea if they will work until we can go back a page
                        self._tempSprite="Green Dude"
                        PygView.changeSprite(self,self._tempSprite)

                    elif self._Sprite4Button.pressed(pygame.mouse.get_pos()):
                        self._tempSprite="Bird"
                        PygView.changeSprite(self,self._tempSprite)

                    elif self._SoundButton.pressed(pygame.mouse.get_pos()):
                        if self._soundOn==True:
                            self._soundOn=False
                        elif self._soundOn==False:
                            self._soundOn=True
                        
                        
                            
                            
            pygame.display.flip()
            pygame.display.update()
            self._fpsClock.tick(30)
            #PygView.play_time(self)
            #ygame.display.flip()
            #pygame.display.update()
            
            
        pygame.quit()

    def play_time(self) :

        milliseconds = self._clock.tick(self._fps)
        self._playtime += milliseconds / 1000.0
        self.draw_text("PLAYTIME: %6.3f SECONDS" %
                         ( self._playtime),350,0)

    
    def changeSprite(self,tempSprite) :
        if tempSprite == "Computer":
            self._spriteObj = pygame.image.load("sprite.png").convert_alpha()
        elif tempSprite == "Mushroom":
            self._spriteObj = pygame.image.load("bot333.gif").convert_alpha()
        elif tempSprite == "Green Dude":
            self._spriteObj = pygame.image.load("bot222.gif").convert_alpha()
        elif tempSprite == "Bird":
            self._spriteObj = pygame.image.load("bot444.gif").convert_alpha()

    def draw_text(self, text, x, y):
        """Center text in window
"""
        fw, fh = self._font.size(text)
        surface = self._font.render(text, True,(0,0,200))
        self._screen.blit(surface, (x,y))
        #self._screen.blit(surface, ((self._width - fw) // 2, (self._height - fh) // 2))


    def SetUpImage(self) :
        """ Set up images for the background
"""
        self._menu=pygame.image.load('Concept_Art4.png') # load the image
        self._menu=pygame.transform.scale(self._menu,(600,400)) # change the size of the image in terms of height and width

        self._maze=pygame.image.load('Concept_Art9.png') # Same as above
        self._maze=pygame.transform.scale(self._maze,(569,369))


    def SetUpButtonMain(self):
        self._playButton.create_button(self._screen,(173,216,230),30,95,100,25,6,'Play',(0,0,0)) #surface,colour, x, y, length, height, width, text. text colour
        self._InstructButton.create_button(self._screen,(173,216,230),30,180,155,25,8,'Instructions',(0,0,0))
        self._OptionButton.create_button(self._screen,(173,216,230),30,250,100,20,7,'Options',(0,0,0))
        self._backButton.create_button(self._screen,(173,216,230),30,200,100,25,6,'Back',(0,0,0))

    def SetUpButtonOptions(self):
        self._Sprite1Button.create_button(self._optionScreen,(173,216,230),180,40,80,25,6,'Sprite1',(0,0,0))  #surface,colour, x, y, length, height, width, text. text colour
        self._Sprite2Button.create_button(self._optionScreen,(173,216,230),290,40,80,25,6,'Sprite2',(0,0,0))  #surface,colour, x, y, length, height, width, text. text colour
        self._Sprite3Button.create_button(self._optionScreen,(173,216,230),390,40,80,25,6,'Sprite3',(0,0,0))  #surface,colour, x, y, length, height, width, text. text colour
        self._Sprite4Button.create_button(self._optionScreen,(173,216,230),490,40,80,25,6,'Sprite4',(0,0,0))  #surface,colour, x, y, length, height, width, text. text colour
        self._SoundButton.create_button(self._optionScreen,(173,216,230),200,90,100,25,6,'Sound',(0,0,0))  #surface,colour, x, y, length, height, width, text. text colour
        self._backButton.create_button(self._screen,(173,216,230),30,200,100,25,6,'Back',(0,0,0))
    
    def SetUpButtonGamePlay(self):
        self._DictionaryButton.create_button(self._mazeScreen,(173,216,255),400,55,160,82,8,'Dictionary',(0,0,0))
        self._HelpButton.create_button(self._mazeScreen,(173,216,230),400,150,160,82,8,'Help',(0,0,0))
        self._RunButton.create_button(self._mazeScreen,(173,216,230),400,245,160,115,8,'Run',(0,0,0))
        

    def loadLevel(self, levelNum):
        levelimages = ['Concept_Art3.png','Concept_Art5.png','Concept_Art6.png','Concept_Art7.png','Concept_Art8.png']
        self._map=pygame.image.load(levelimages[levelNum]) # Same as above
        self._map=pygame.transform.scale(self._map,(self._infoObj.current_w,self._infoObj.current_h))


if __name__ == '__main__':
    
    # call with the height, width of window and fps 400,600,30
    PygView(400,600,30).run()
