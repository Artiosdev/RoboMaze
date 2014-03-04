import pygame, Buttons, robot, grid

####

class PygView():



  
    def __init__(self,height, width, fps):
        """Initialize pygame, window, background, font,...
        """
        pygame.init() # define the pygame interface
        pygame.display.set_caption("RoboGuide - Press ESC to quit")
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF) #initialise the screen
        self._mazeScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF)
        self._menu = 0
        self._maze= 0
        self._instructions=0
        self._clock = pygame.time.Clock()
        self._fps = fps  #Frames per second
        self._playtime = 0.0
        self._font = pygame.font.SysFont('mono', self._height // 30, bold=True) #set the font for the text
        self._playButton=Buttons.Button() #create an object of Button
        self._InstructButton=Buttons.Button()
        self._OptionButton=Buttons.Button()
        self._ReturnButton=Buttons.Button()
        self._DictionaryButton=Buttons.Button()
        self._HelpButton=Buttons.Button()
        self._RunButton=Buttons.Button()
        self._map=0
        self._fpsClock = pygame.time.Clock()
        self._spriteObj = pygame.image.load("sprite.png").convert_alpha()

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
            self._soundObj2.play()
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
        PygView.SetUpButtonGamePlay(self)
        while running:

            self._playerPosition = self._robot1.getPosition()
            



            if(self._menuMode == True):
                self._screen.blit(self._menu, (0, 0))

        
            
            if(self._gamemode == True):
                self._screen.blit(self._map,(0,0))
                self._screen.blit(self._spriteObj,(self._playerPosition[0]*42,self._playerPosition[1]*20))
                
            
            for event in pygame.event.get():
               

                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self._playButton.pressed(pygame.mouse.get_pos()): 
                        self._width=569                                                                     # new width for the screen
                        self._height= 369                                                                    # new height for the screen
                        self._menu=pygame.transform.scale(self._menu,(0,0))                                  # resizing the menu screen so it disappear
                        self._mazeScreen = pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF)
                        pygame.display.flip()                                                                # display the changes to the menu
                        self.loadLevel(0)#the number will have to change using a counter
                        #pygame.display.flip()
                        #pygame.display.update()                                                              # update the change to the screen
                        self._gamemode = True
                        self._menuMode = False
                        self._level1.initialiseGrid()

                        
                    elif self._DictionaryButton.pressed(pygame.mouse.get_pos()) :                        
                        self._width=569
                        self._height=369
                        self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF) # set up a screen with the new width and height
                        pygame.display.flip()                                                                # display the changes to the menu
                        self._screen.blit(self._screen,(0,0))
                        self._screen.fill((173,216,230))
                        pygame.display.flip()
                        pygame.display.update()       


                    elif self._HelpButton.pressed(pygame.mouse.get_pos()) :
                        self._width=569
                        self._height=369
                        self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF) # set up a screen with the new width and height
                        pygame.display.flip()                                                                # display the changes to the menu
                        self._screen.blit(self._screen,(0,0))
                        self._screen.fill((173,216,230))
                        pygame.display.flip()
                        pygame.display.update()


                    elif self._RunButton.pressed(pygame.mouse.get_pos()) :
                        self._width=569
                        self._height=369
                        self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF) # set up a screen with the new width and height
                        pygame.display.flip()                                                                # display the changes to the menu
                        self._screen.blit(self._screen,(0,0))
                        self._screen.fill((173,216,230))
                        pygame.display.flip()
                        pygame.display.update()
                            
                        
                        
                            

                    elif self._InstructButton.pressed(pygame.mouse.get_pos()):
                        self._width=900
                        self._height=400
                        self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF) # set up a screen with the new width and height
                        self._menu=pygame.transform.scale(self._menu,(0,0))                                  # resizing the menu screen so it disappear
                        self._screen.blit(self._menu,(0,0))                                                  # apply the changes with menu to the screen
                        pygame.display.flip()                                                                # display the changes to the menu
                        self._screen.blit(self._screen,(0,0))                                                # apply the changes with maze to the screen
                        
                        self._screen.fill((173,216,230))
                        self.draw_text("Instructions", 400,0)
                        self.draw_text("Welcome to Robo-Guide. A game that will test your compatibility with the Computer Science",20,40)
                        self.draw_text("undergraduate course at Oxford Brookes. The game will require you to safely navigate a",20,60)
                        self.draw_text("robot through hazardous courses by typing in commands with your keyboard.",20,80)
                        self.draw_text("The code you type into the game will not require knowledge of any high level programming language.",20,100)
                        self.draw_text("The code inputted will be very straightforward and the game will be able to assist you.",20,120)
                        self.draw_text("if you’re stuck when you press the help button during the game.The courses will have an end point",20,140)
                        self.draw_text("that the user is supposed to reach, getting to this point faster will reward the player,",20,160)
                        self.draw_text("however by taking these shortcuts you may be required to answer questions related to the",20,180)
                        self.draw_text("computer science course. Incorrect answers will result in failure in the level. Once the end point ",20,200)
                        self.draw_text("is reached a final question is asked, a correct answer will allow the player to proceed to the next level",20,220)
                        self.draw_text("where the difficulty of the questions escalate.",20,240)
                                       
                        pygame.display.flip()
                        pygame.display.update()

                         

                    elif self._OptionButton.pressed(pygame.mouse.get_pos()) :
                        self._width=900
                        self._height=400
                        self._screen= pygame.display.set_mode((self._width, self._height), pygame.DOUBLEBUF) # set up a screen with the new width and height
                        self._menu=pygame.transform.scale(self._menu,(0,0))                                  # resizing the menu screen so it disappear
                        self._screen.blit(self._menu,(0,0))                                                  # apply the changes with menu to the screen
                        pygame.display.flip()                                                                # display the changes to the menu
                        self._screen.blit(self._screen,(0,0))
                        self._screen.fill((173,216,230))
                        self.draw_text("Option", 450,0)
                        pygame.display.flip()
                        pygame.display.update()

                if (event.type==pygame.KEYDOWN):

                    if (event.key==pygame.K_LEFT):
                        self._spriteObj = self.rotateLeft(self._spriteObj)    
                    elif (event.key==pygame.K_RIGHT): 
                        self._spriteObj = self.rotateRight(self._spriteObj)
                    elif (event.key==pygame.K_UP):
                        self.moveForward()
                    elif (event.key==pygame.K_SPACE):
                        self.repeatUntilCollision()
                   

                    
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
        self._playButton.create_button(self._screen,(173,216,230),30,95,100,25,6,'Play',(0,0,0))  #surface,colour, x, y, length, height, width, text. text colour
        self._InstructButton.create_button(self._screen,(173,216,230),30,180,155,25,8,'Instructions',(0,0,0))
        self._OptionButton.create_button(self._screen,(173,216,230),30,250,100,20,7,'Options',(0,0,0))

    def SetUpButtonGamePlay(self):
        self._DictionaryButton.create_button(self._mazeScreen,(173,216,255),400,55,160,82,8,'Dictionary',(0,0,0))
        self._HelpButton.create_button(self._mazeScreen,(173,216,230),400,150,160,82,8,'Help',(0,0,0))
        self._RunButton.create_button(self._mazeScreen,(173,216,230),400,245,160,115,8,'Run',(0,0,0))

    def loadLevel(self, levelNum):
        levelimages = ['Concept_Art3.png','Concept_Art5.png','Concept_Art6.png','Concept_Art7.png','Concept_Art8.png']
        self._map=pygame.image.load(levelimages[levelNum]) # Same as above
        self._map=pygame.transform.scale(self._map,(569,369))

    
####

if __name__ == '__main__':
    
    # call with the height, width of window and fps 400,600,30
    PygView(400,600,30).run()
