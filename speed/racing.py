import pygame

import random

pygame.init()

#TO DO: Make questions and make them random and fix go back into incorrect bug.
#Title
pygame.display.set_caption('Average Speed Game')

#Screen 
screenWidth=900
screenHeight=500
win=pygame.display.set_mode((screenWidth,screenHeight))

#Framerate
clock= pygame.time.Clock()

#background image
bg=pygame.image.load('C:\\Users\\18597\\Desktop\\My Python Scripts\\speed\\bg.png')

#button colors
buttonWhite=(255,255,255)
buttonPink=(255,182,193)

class car(object):
    def __init__(self):
        self.x=0 
        self.y=300
        self.image=pygame.image.load('C:\\Users\\18597\\Desktop\\My Python Scripts\\speed\\car.png')

            
#Car Instance
global racer
racer=car()

class question(object):
    def __init__(self,b,c,d):
        self.a=['Time/Distance','Direction+Time','13mph']
        self.b=b
        self.c=c
        self.d=d
        self.q=['What is the Formula for Speed','What is the Formula for Velocity', 'What is the average speed of 13miles in 6 min.']
        self.font=pygame.font.SysFont('Courier',30,True,False)
        
    def draw(self,win):
        self.font
        q1Text= self.font.render(self.q[0],1,(255,182,193))
        win.blit(q1Text,(200,50))
        button('',130,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco')
        q1TextA= self.font.render(self.a[0],1,(255,182,193))
        win.blit(q1TextA,(150,150))
        button('',530,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co')
        q1TextB= self.font.render(self.b,1,(255,182,193))
        win.blit(q1TextB,(550,150))
        button('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco')
        q1TextC= self.font.render(self.c,1,(255,182,193))
        win.blit(q1TextC,(150,250))
        button('',530,240,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco')
        q1TextD= self.font.render(self.d,1,(255,182,193))
        win.blit(q1TextD,(550,250))
global q1
q1=question('B.Distance/Time','C.Accleration/Time','D.Distance+Time')  

    #Button for Start
def button(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co':
                    correctPage()
                elif action == 'inco':
                    incorrectPage()
        else:       
            pygame.draw.rect(win, active,(x,y,w,h))
        buttonText= pygame.font.SysFont('Courier',30,True,False)
        buttonType= buttonText.render(msg,1,(activeT))
        buttonText2= pygame.font.SysFont('Courier',30,True,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))
        if x+w> mouse[0] >x and y+h>mouse[1] > y:
            win.blit(buttonType2,(xT,yT))
        else:
            win.blit(buttonType,(xT,yT))            
        buttonText2= pygame.font.SysFont('Courier',30,True,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))

def buttonBack(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'backQ':
                    gameLoop()
                elif action == 'start':
                    gameLoop()
        else:       
            pygame.draw.rect(win, active,(x,y,w,h))
        buttonText= pygame.font.SysFont('Courier',30,True,False)
        buttonType= buttonText.render(msg,1,(activeT))
        buttonText2= pygame.font.SysFont('Courier',30,True,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))
        if x+w> mouse[0] >x and y+h>mouse[1] > y:
            win.blit(buttonType2,(xT,yT))
        else:
            win.blit(buttonType,(xT,yT))            
        buttonText2= pygame.font.SysFont('Courier',30,True,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))

def buttonStart(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'start':
                    gameLoop()
        else:       
            pygame.draw.rect(win, active,(x,y,w,h))
        buttonText= pygame.font.SysFont('Courier',30,True,False)
        buttonType= buttonText.render(msg,1,(activeT))
        buttonText2= pygame.font.SysFont('Courier',30,True,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))
        if x+w> mouse[0] >x and y+h>mouse[1] > y:
            win.blit(buttonType2,(xT,yT))
        else:
            win.blit(buttonType,(xT,yT))            
        buttonText2= pygame.font.SysFont('Courier',30,True,False)
        buttonType2= buttonText2.render(msg,1,(inactiveT))
        
        
def start():
    start=True
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        startFont=pygame.font.SysFont('Courier',50,True,False)
        startText= startFont.render('Start Game',1,(255,182,193))
        win.blit(startText,(315,100))
        buttonStart('Start',275,220,300,50,buttonWhite,buttonPink,380,230,buttonPink,buttonWhite,'start')
        pygame.display.update()
        clock.tick(15)

def incorrectPage():
    inco=True
    while inco:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                inco=False
        win.blit(bg,(0,0))
        incoFont=pygame.font.SysFont('Courier',50,True,False)
        incoText= incoFont.render('Incorrect',1,(255,182,193))
        win.blit(incoText,(315,100))
        buttonBack('Back',275,220,300,50,buttonWhite,buttonPink,380,230,buttonPink,buttonWhite,'backQ')
        if racer.x>=200:
            racer.x-=200
            win.blit(racer.image,(racer.x,270))
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)
    

def correctPage():
    co=True
    while co:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                co=False
        win.blit(bg,(0,0))
        coFont=pygame.font.SysFont('Courier',50,True,False)
        coText= coFont.render('Correct!',1,(255,182,193))
        win.blit(coText,(315,100))
        buttonBack('Next Question',275,220,300,50,buttonWhite,buttonPink,380,230,buttonPink,buttonWhite,'backQ')
        racer.x=+200
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)


def redrawGameWin():
    win.blit(bg,(0,0))
    q1.draw(win)
    win.blit(racer.image,(racer.x,270))
    pygame.display.update()
    clock.tick(15)

def gameLoop():
    run= True
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run=False
        redrawGameWin()

start()
pygame.quit()

