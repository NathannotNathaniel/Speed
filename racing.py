import pygame

import random

pygame.init()

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

class question(object):
    def __init__(self,q,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.q=q
        self.font=pygame.font.SysFont('Courier',30,True,False)
        self.mouse=pygame.mouse.get_pos()
        self.click=pygame.mouse.get_pressed()
        self.action=None 
        self.button=pygame.draw.rect(win,(255,255,255),(150,150,100,100))
        self.answer='Answer-'

    def draw(self,win):
        if newQ ==True:
            self.font
            q1Text= self.font.render(self.q,1,(255,182,193))
            win.blit(q1Text,(200,50))
            q1TextA= self.font.render(self.a,1,(255,182,193))
            win.blit(q1TextA,(150,150))
            q1TextB= self.font.render(self.b,1,(255,182,193))
            win.blit(q1TextB,(550,150))
            q1TextC= self.font.render(self.c,1,(255,182,193))
            win.blit(q1TextC,(150,250))
            q1TextD= self.font.render(self.d,1,(255,182,193))
            win.blit(q1TextD,(550,250))
            q1Ans=self.font.render(self.answer+input(),1,(255,182,193))
            win.blit(q1Ans,(200,600))
            

def correctPage():
    print('sucessful')
def redrawGameWin():
    win.blit(bg,(0,0))
    q1.draw(win)
    pygame.display.update()

def gameLoop():
    global newQ
    newQ=True
    global q1
    q1=question('What is the formula for speed','A.Time/Distance','B.Distance/Time','C.Accleration/Time','D.bruh')
    global font
    q1.font
    run= True
    while run:
        clock.tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run=False

        redrawGameWin()

gameLoop()
pygame.quit()

