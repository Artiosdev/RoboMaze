class spriteMovement:
    def __init__(self,x,y):
        self.playerposition = [x,y]
        self.direction = 0
        self.moveX = 0
        self.moveY = 0

    def getPosition(self):
        return self.playerposition
    def getDirection(self):
        return self.direction;
    def setPosition(self,playerposition):
        self.playerposition = playerposition
    def rotateLeft(self):
        if self.direction==0:
            self.direction=360 
        self.direction-=90    
    def rotateRight(self):
        self.direction+=90
        if self.direction==360:
            self.direction=0

    def moveForward(self):
        if self.direction == 270:
            if self.playerposition[1]==0:
                self.moveY=0
            else: 
                self.moveY = -1
        elif self.direction == 90:
            if self.playerposition[1]==9:
               self.moveY=0
            else:
               self.moveY = 1
        elif self.direction == 180:
            if self.playerposition[0]==0:
               self.moveX=0
            else: 
               self.moveX = -1
        elif self.direction == 0:
            if self.playerposition[0]==9:
                self.moveX=0
            else: 
                self.moveX = 1

        self.playerposition[0] += self.moveX
        self.playerposition[1] += self.moveY

        self.moveX = 0
        self.moveY = 0

    def CheckCollisions(self):
        if self.direction == 270:
               self.moveY = -1
        elif self.direction == 90:
               self.moveY = 1
        elif self.direction == 180:
               self.moveX = -1
        elif self.direction == 0:
               self.moveX = 1

        position = []       

        position.append(self.playerposition[0] + self.moveX)
        position.append(self.playerposition[1] + self.moveY)

        self.moveX = 0
        self.moveY = 0

        return position
        
        
        
    
        
    
        
         


        
    



   

                
