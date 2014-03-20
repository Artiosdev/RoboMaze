class Question:
    def __init__(self,question,answers,multichoice,correctanswer):
        self.question = question
        self.answers = answers
        self.multiChoice = multichoice
        self.correctAnswer = correctanswer


    def getQuestion(self,question):
        return self.question

    def getAnswer(self,question):
        return self.answer[0]

    def getMode(self):
        return self.multiChoice
    def getChoice(self,num):
        print(num)
        return self.answers[num]
    
    def checkAnswer(self,userAnswer):
        if self.multiChoice == False:
            correct = False
            i = 0
            for i in range(len(self.answers)):
                userAnswer = userAnswer.replace(" ", "")
                userAnswer = userAnswer.lower()
                if(userAnswer.find(self.answers[i]) != -1):
                    correct = True
            return correct
        else:
            if userAnswer.find(self.correctAnswer) != -1:
                return True
            else:
                return False
            
            


                
            
            
    
            
        


        
    
