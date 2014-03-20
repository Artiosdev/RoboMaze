import pygame,Buttons,random,sys,question,eztext



green = (118,210,0)
bg = pygame.image.load("quizbg.png")





class questionScreen():

   
    

    def __init__(self,width,height,questionsAsked):

        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF) #initialise the screen
        self.ButtonA = Buttons.Button()
        self.ButtonB = Buttons.Button()
        self.ButtonC = Buttons.Button()
        self.ButtonD = Buttons.Button()
        self.exitButton = Buttons.Button()
        self.questions = []
        self.currentQuestion = None
        self.myfont = pygame.font.SysFont("monospace", 15)
        self.multiChoiceMode = True
        self.fpsClock = pygame.time.Clock() 
        ## My TextBox Variable
        self.txtbx = eztext.Input(maxlength=30, color=green, prompt='Answer:')
        self.tick=pygame.image.load('tick.png').convert_alpha()
        self.cross=pygame.image.load('cross.png').convert_alpha()
        self.correct = False
        self.timer = 300
        self.bg = pygame.image.load("quizbg.png")
        self.bg2 = pygame.image.load("quizbg2.png")
        self.bg2 = pygame.transform.scale(self.bg2,(width,height))
        self.bg = pygame.transform.scale(self.bg,(width,height))
        self.currentbg = self.bg
        self.score = 0.0;
        self.questioncount = 0;
        self.questionsAsked = questionsAsked
        self.option1 = ""
        self.option2 = ""
        self.option3 = ""
        self.option4 = ""
        self.endGame = False
        
        
        

        
        self.txtbx.set_pos(0,self.height/4*3)

        self.loadQuestions()
        self.askQuestion()


        self.label = self.myfont.render(self.currentQuestion.question, 1, green)
        self.label2 = self.myfont.render("Your Score is" + str(self.score), 1, green)
        


    def run(self):
        """The mainloop
        """
        running = True

        
       
            

        
        while running:
            self.screen.blit(self.currentbg,(0,0))
            

            if (self.endGame == True):
                self.exitButton.create_button(self.screen,(173,216,230),self.width/4,self.height/8*4,self.width/2,self.height/8,6,"Quit Game",(0,0,0))
                score = str(self.getScore()) + "%" 
                self.label2 = self.myfont.render("Your Score is " + score, 1, green)
                self.screen.blit(self.label2, (10, self.height/4))
            else:
                self.printQuestion()
                self.multiChoiceMode = self.currentQuestion.getMode()
                if(self.multiChoiceMode == True):
                    self.ButtonA.create_button(self.screen,(173,216,230),0,self.height/8*3,self.width/2,self.height/8,18,self.option1,(0,0,0)) #surface,colour, x, y, length, height, width, text. text colour
                    self.ButtonB.create_button(self.screen,(173,216,230),self.width/2,self.height/8*3,self.width/2,self.height/8,18,self.option2,(0,0,0))
                    self.ButtonC.create_button(self.screen,(173,216,230),0,self.height/8*4,self.width/2,self.height/8,18,self.option3,(0,0,0))
                    self.ButtonD.create_button(self.screen,(173,216,230),self.width/2,self.height/8*4,self.width/2,self.height/8,18,self.option4,(0,0,0))
                    self.currentbg = self.bg2
                else:
                    self.txtbx.draw(self.screen)
                    self.currentbg = self.bg
                
               
                


            

            

            

            if(self.timer < 100):
                if(self.correct == True):
                    if ((self.timer % 3) == 0):
                        self.screen.blit(self.tick,(50,100))
                else:
                    if ((self.timer % 3) == 0):
                        self.screen.blit(self.cross,(50,100))
                self.timer = self.timer + 1


            
           
               

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                             endgame = self.checkAnswer(self.txtbx.getText())
                             if endgame:
                                 self.endGame = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.endGame == True):
                        if self.exitButton.pressed(pygame.mouse.get_pos()):
                            running = False
                    if(self.multiChoiceMode == True):
                        if self.ButtonA.pressed(pygame.mouse.get_pos()):
                           endgame = self.checkAnswer(self.currentQuestion.getChoice(0))
                        if self.ButtonB.pressed(pygame.mouse.get_pos()):
                           endgame = self.checkAnswer(self.currentQuestion.getChoice(1))
                        if self.ButtonC.pressed(pygame.mouse.get_pos()):
                           endgame = self.checkAnswer(self.currentQuestion.getChoice(2))
                        if self.ButtonD.pressed(pygame.mouse.get_pos()):
                            endgame = self.checkAnswer(self.currentQuestion.getChoice(3))   
                        if endgame:
                             self.multiChoiceMode = False
                             self.endGame = True     
                    
                            
                        

    

                    
                       
            self.txtbx.update(events) 
                                                                               
            pygame.display.flip()
            pygame.display.update()

        
        pygame.quit()
        sys.exit()


    def loadQuestions(self):
        q1 = question.Question("Please name any common network topology?",["star","bus","ring"],False,None)
        q2 = question.Question("what is 9 in binary?",["1001"],False,None)
        q3 = question.Question("What does RAM stand for?",["randomaccessmemory"],False,None)
        q4 = question.Question("What computer component proccess graphics?",["CPU","GPU","RAM","Hard Drive"],True,"GPU")
        q5 = question.Question("Which one of these is not a type of" + "\n" + "software testing?",["Black Box Testing","White Box Testing","Sound Testing","Unit Testing"],True,"Sound Testing")
        q6 = question.Question("What is the result of this binary addition?" + "\n" + "101010" + "\n" + "010011" + "\n" + "________",["111101"],False,None)
        
        self.questions.append(q1)
        self.questions.append(q2)
        self.questions.append(q3)
        self.questions.append(q4)
        self.questions.append(q5)
        self.questions.append(q6)
        
    def askQuestion(self):
        num = random.randint(0,len(self.questions)) - 1
        self.currentQuestion = self.questions[num]
        if( self.currentQuestion.getMode() == True):
            self.option1 = self.currentQuestion.getChoice(0)
            self.option2 = self.currentQuestion.getChoice(1)
            self.option3 = self.currentQuestion.getChoice(2)
            self.option4 = self.currentQuestion.getChoice(3)
        self.printQuestion()

    def printQuestion(self):
        if(len(self.currentQuestion.question) > 35):
            lines = self.currentQuestion.question.split("\n")
            for i in range(len(lines)):
                self.label = self.myfont.render(lines[i], 1, green)
                self.screen.blit(self.label, (10, self.height/8 + (i * 20)))
        else:
            self.label = self.myfont.render(self.currentQuestion.question, 1, green)
            self.screen.blit(self.label, (10, self.height/4))
            
        
    def checkAnswer(self,answer):
        self.correct = self.currentQuestion.checkAnswer(answer)
        self.timer = 0
        self.questioncount = self.questioncount + 1
        if self.correct == True:
            self.score = self.score + 1

        if(self.questioncount < self.questionsAsked): 
            self.askQuestion()
            return False
        else:
            return True

    def getScore(self):
        score = self.score/self.questionsAsked * 100
        return score
  
      
           
            
        

questionScreen(400,600,10).run()




    

