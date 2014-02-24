import pygame, Buttons

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


    def run(self):
        """The mainloop
        """
        running = True
        PygView.SetUpButtonMain(self)
        PygView.SetUpImage(self)
        PygView.SetUpButtonGamePlay(self)
        while running:
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
                        self._mazeScreen.blit(self._maze,(0,0))                                              # apply the changes with maze to the screen
                        pygame.display.flip()
                        pygame.display.update()                                                              # update the change to the screen

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

                    
                    

            self._screen.blit(self._menu,(0,0))
                    
            pygame.display.flip()
            pygame.display.update()

            #PygView.play_time(self)
            #ygame.display.flip()
            #pygame.display.update()
            
            self._screen.blit(self._menu, (0, 0))
            
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

        self._maze=pygame.image.load('GamePlayScreen.png') # Same as above
        self._maze=pygame.transform.scale(self._maze,(569,369))


    def SetUpButtonMain(self):
        self._playButton.create_button(self._screen,(173,216,230),30,95,100,25,6,'Play',(0,0,0))  #surface,colour, x, y, length, height, width, text. text colour
        self._InstructButton.create_button(self._screen,(173,216,230),30,180,155,25,8,'Instructions',(0,0,0))
        self._OptionButton.create_button(self._screen,(173,216,230),30,250,100,20,7,'Options',(0,0,0))

    def SetUpButtonGamePlay(self):
        self._DictionaryButton.create_button(self._mazeScreen,(173,216,255),400,55,160,82,8,'Dictionary',(0,0,0))
        self._HelpButton.create_button(self._mazeScreen,(173,216,230),400,150,160,82,8,'Help',(0,0,0))
        self._RunButton.create_button(self._mazeScreen,(173,216,230),400,245,160,115,8,'Run',(0,0,0))

####

if __name__ == '__main__':
    
    # call with the height, width of window and fps
    PygView(400,600, 30).run()

