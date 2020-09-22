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
        self.endImage=pygame.image.load('C:\\Users\\18597\\Desktop\\My Python Scripts\\speed\\Lightning_McQueen.png')

            
#Car Instance
global racer
racer=car()

global font 
font= pygame.font.SysFont('Courier',30,True,False)


def quest1():
    global q1 
    q1=True
    while q1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        q1Text= font.render("What is the Formula for Average Speed?",1,(255,182,193))
        win.blit(q1Text,(200,50))
        buttonIn('',130,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco')
        q1TextA= font.render('Time/Distance',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonCo('',530,150,270,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co')
        q1TextB= font.render('Distance/Time',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonIn('',130,240,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco')
        q1TextC= font.render('Distance-Time',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn('',530,240,360,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco')
        q1TextD= font.render('Direction/Distance',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=0
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
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
                    quest2()
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

def buttonIn(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco':
                    quest1()
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

global font2 
font2= pygame.font.SysFont('Courier',30,True,False)

def quest2():
    q2=True
    while q2:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        q1Text= font2.render("What is the Formula for Velocity?",1,(255,182,193))
        win.blit(q1Text,(200,50))
        buttonIn2('',130,150,330,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco2')
        q1TextA= font2.render('Direction x Speed',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonIn2('',530,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco2')
        q1TextB= font2.render('Distance/Time',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonCo2('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co2')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= fontC.render('Distance/Time + Direction',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn2('',530,240,320,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco2')
        q1TextD=fontC.render('Direction/Distance +Time',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=100
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo2(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co2':
                    quest3()
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

def buttonIn2(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco2':
                    quest2()
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

def quest3():
    q3=True
    while q3:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1Text= fontC.render("Jimmy ran a 40 yard dash in 6.30 Seconds. What is his time in yrd/s?",1,(255,182,193))
        win.blit(q1Text,(50,50))
        buttonCo3('',130,150,330,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co3')
        q1TextA= font2.render('6.34',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonIn3('',530,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco3')
        q1TextB= font2.render('6.01',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonIn3('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco3')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= fontC.render('6',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn3('',530,240,320,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco3')
        q1TextD=fontC.render('6.43',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=200
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)
def buttonCo3(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co3':
                    quest4()
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

def buttonIn3(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco3':
                    quest3()
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

def quest4():
    q4=True
    while q4:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1Text= fontC.render("The School bus went 30 miles in 20 minutes, with stops and starts.",1,(255,182,193))
        win.blit(q1Text,(50,50))
        buttonIn4('',130,150,330,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco4')
        q1TextA= font2.render('Speed',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonCo4('',530,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co4')
        q1TextB= font2.render('Acceleration',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonIn4('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco4')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= fontC.render('Velocity',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn4('',530,240,320,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco4')
        q1TextD=font2.render('Slow',1,(255,182,193))
        win.blit(q1TextD,(630,250))
        racer.x=300
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)
    print('hello')

def buttonCo4(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co4':
                    quest5()
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

def buttonIn4(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco4':
                    quest4()
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

def quest5():
    q5=True
    while q5:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1Text= font2.render("A biker trailed 150 miles North in 3 months",1,(255,182,193))
        win.blit(q1Text,(50,50))
        buttonIn5('',130,150,330,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco5')
        q1TextA= font2.render('Average Speed',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonIn5('',530,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco5')
        q1TextB= font2.render('Acceleration',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonCo5('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co5')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= font2.render('Velocity',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn5('',530,240,320,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco5')
        q1TextD=fontC.render('Pythagorem Theorem',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=400
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo5(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co5':
                    quest6()
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

def buttonIn5(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco5':
                    quest5()
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

def quest6():
    q6=True
    while q6:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1Text= font2.render("What is the Format for Writing Acceleration",1,(255,182,193))
        win.blit(q1Text,(50,50))
        buttonIn6('',130,150,100,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco6')
        q1TextA= font2.render('m/s',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonCo6('',530,150,130,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco6')
        q1TextB= font2.render('m/s/m',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonIn6('',130,240,100,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco6')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= font2.render('m/s3',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonCo6('',530,240,100,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co6')
        q1TextD=font2.render('m/s2',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=500
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo6(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co6':
                    quest7()
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

def buttonIn6(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco6':
                    quest6()
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

def quest7():
    q7=True
    while q7:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1Text= font2.render("Trevor Bauer threw a pitch that went 93mph",1,(255,182,193))
        win.blit(q1Text,(50,50))
        buttonIn7('',130,150,330,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco7')
        q1TextA= font2.render('Acceleration',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonIn7('',530,150,300,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco7')
        q1TextB= font2.render('Velocity',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonCo7('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co7')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= font2.render('Speed',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn7('',530,240,320,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco7')
        q1TextD=font2.render('100mph',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=600
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo7(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co7':
                    quest8()
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

def buttonIn7(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco7':
                    quest7()
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

def quest8():
    q8=True
    while q8:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',17,True,False)
        q1Text= fontC.render("Mike drove to Cinncinati from Houston (300mi) in 30 hours. What was his velocity?",1,(255,182,193))
        win.blit(q1Text,(50,50))
        buttonIn8('',130,150,330,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco8')
        q1TextA= font2.render('10mph North',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonIn8('',530,150,330,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco8')
        q1TextB= font2.render('30 mph NorthEast',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonIn8('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco8')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= font2.render('100mph Northwest',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonCo8('',530,240,320,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co8')
        q1TextD=font2.render('10mph Northeast',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=700
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo8(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co8':
                    quest9()
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

def buttonIn8(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco8':
                    quest8()
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
print('hello?')
def quest9():
    q9=True
    while q9:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1Text= font2.render("What does Acceleration Measure?",1,(255,182,193))
        win.blit(q1Text,(180,50))
        buttonIn9('',130,150,340,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco9')
        q1TextA= fontC.render('The Change in Acceleration',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonCo9('',530,150,360,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co9')
        q1TextB= fontC.render('The Change in Velocity/Speed',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonIn9('',130,240,350,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco9')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= fontC.render('Average Speed',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn9('',530,240,320,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco9')
        q1TextD=fontC.render('The Area of a Trapezoid',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=750
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo9(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co9':
                    quest10()
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

def buttonIn9(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco9':
                    quest9()
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

def quest10():
    q10=True
    while q10:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1Text= fontC.render("How many miles did Wayne travel if he went for 38hrs at 40mph?",1,(255,182,193))
        win.blit(q1Text,(50,50))
        buttonIn10('',130,150,125,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco10')
        q1TextA= font2.render('3719',1,(255,182,193))        
        win.blit(q1TextA,(150,150))
        buttonIn10('',530,150,125,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco10')
        q1TextB= font2.render('1683',1,(255,182,193))
        win.blit(q1TextB,(550,150))
        buttonCo10('',130,240,125,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'co10')
        fontC=pygame.font.SysFont('Courier',20,True,False)
        q1TextC= font2.render('1520',1,(255,182,193))
        win.blit(q1TextC,(150,250))
        buttonIn10('',530,240,125,50,buttonWhite,buttonWhite,145,145,buttonPink,buttonWhite,'inco10')
        q1TextD=font2.render('1',1,(255,182,193))
        win.blit(q1TextD,(550,250))
        racer.x=800
        win.blit(racer.image,(racer.x,270))
        pygame.display.update()
        clock.tick(15)

def buttonCo10(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'co10':
                    gameEnd()
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

def buttonIn10(msg,x,y,w,h,inactive,active,xT,yT,inactiveT,activeT,action=None):
        #Use location of mouse to track the button
        mouse= pygame.mouse.get_pos()
        #Tracks mouse clicks
        click=pygame.mouse.get_pressed() 
        #0 is x, 1 is y, 2 is width, 3 is height
        if x+w> mouse[0] >x and y+h>mouse[1]>y:
            pygame.draw.rect(win, inactive,(x,y,w,h))
            #Click[0] is left mouse click
            if click[0] == 1 and action!= None:
                if action == 'inco10':
                    quest10()
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

def gameEnd():
    end=True
    while end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(bg,(0,0))
        font=pygame.font.SysFont('Courier',50,True,False)
        endText= font.render("Congratulations!",1,(255,182,193))
        win.blit(endText,(200,50))
        endText= font.render("Your Car made it to the End!",1,(255,182,193))
        win.blit(endText,(50,200))
        win.blit(racer.endImage,(300,270))
        pygame.display.update()
        clock.tick(15)
quest1()
pygame.quit()

