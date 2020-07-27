import numpy as np
import pygame as pg
from pygame.locals import *
pg.init()
disp_wid=700
disp_height=700
win=pg.display.set_mode((disp_wid,disp_height))
pg.display.set_caption("CONNECT 4")
surf=pg.image.load('connect4.png').convert()
surf=pg.transform.smoothscale(surf,(700,600))

a=np.zeros([6,7],dtype='int16')
black=(0,0,0)
red=(175,0,0)
br_red=(255,0,0)
green=(0,175,0)
br_green=(0,255,0)
blue=(0,0,200)
yellow=(255,255,0)
#dimensions
rad=40
connectB=(0,70,700,630)
c=[5]*7

def draw():
	for i in range(7):
		for j in range(6):
			newCenter=(50+(100*i),150+(100*j))
			pg.draw.circle(win,black,newCenter,rad,rad)

def textSize(msg,x,y,w,h,num):
	smallText=pg.font.Font("freesansbold.ttf",num) #setting text size
	textSurf,textRect=text_obj(msg,smallText) #getting renderedtext and textdim
	textRect.center=((x+(w/2)),(y+(h/2))) # text centering
	win.blit(textSurf,textRect) #text display

def text_obj(text,font):
	textSurf=font.render(text,True,black)  #rendering into display-able form
	return textSurf,textSurf.get_rect()   # text dimensions

def button(msg,x,y,w,h,ic,ac,action=None):
	mouse=pg.mouse.get_pos()
	#print(mouse)
	click=pg.mouse.get_pressed()
	if x+w > mouse[0]>x and y+h>mouse[1]>y: #if mouse in rect area
		pg.draw.rect(win,ac,(x,y,w,h))
		textSize(msg,x,y,w,h,21)   #active color
		if click[0]==1 and action!=None:
			if action=="play":
				game_loop()
				main()
			elif action=="back":
				return 1
			elif action=="quit":
				exit()
	else:
		pg.draw.rect(win,ic,(x,y,w,h))#inactive color
		textSize(msg,x,y,w,h,18)   

def check(i,n):
    l=[]
    r=[]
    e=[]
    if(c[n]<=2 and a[c[n]+1,n]==i and a[c[n]+2,n]==i and a[c[n]+3,n]==i):
        return 1
    for x in range(7):
        try:
            l.append(a[c[n]+3-x,n-3+x])
        except IndexError:
            l.append(0)
            pass
        try:
            r.append(a[c[n]-3+x,n-3+x]) 
        except IndexError:
            r.append(0)
            pass
        try:
            e.append(a[c[n],x])
        except IndexError:
            e.append(0)
            pass
    s=str(i)*4
    print(f"str=",s)
    ls=''.join([str(int(n)) for n in l])
    print(ls)
    rs=''.join([str(int(n)) for n in r])
    print(rs)
    es=''.join([str(int(n)) for n in e])
    print(es)
    if(s in ls or s in rs or s in es):
        return 1
    return 0

def game_loop():
	player=yellow
	p=2
	running=True
	win.fill((0,0,0))
	pg.draw.rect(win,blue,connectB)
	draw()
	pg.display.update()
	myfont = pg.font.SysFont('courier',70)
	clock = pg.time.Clock()
	while(running):
		b=button("Back",20,10,60,30,green,br_green,"back")
		if b==1:
			return

		mouse=pg.mouse.get_pos()
		click=pg.mouse.get_pressed()


		for event in pg.event.get():
			if event.type==pg.MOUSEBUTTONDOWN:
				if player==yellow:
					player=br_red
					p=1
				elif player==br_red:
					player=yellow
					p=2

				mRow=int(mouse[1]/100)  
				mCol=int(mouse[0]/100)  
				print(mRow,mCol)
				if (c[mCol]>=0) and mRow>0:
					pg.draw.circle(win,player,(mCol*100+50,c[mCol]*100+150),rad)
					print(a)
					a[c[mCol],mCol]=p
					pg.display.update()
					result=check(p,mCol)
					print(f"result",result)
					c[mCol]=c[mCol]-1
					counter=0
					if result==1:
						while(counter<24):
							counter=counter+1
							if counter%2==0:      #flickering win
								colored=(225,225,225)
							else:
								colored=(0,0,0)
							if player==yellow:
								textsurface = myfont.render("YELLOW WINS!", False, colored)
								win.blit(textsurface,(130,0))
								pg.display.update()
							else:
								textsurface = myfont.render("RED WINS!", False, colored)
								win.blit(textsurface,(180,0))
								pg.display.update()
							for event in pg.event.get():
								if event.type==pg.MOUSEBUTTONDOWN:
									if event.type==pg.QUIT:
										sys.exit()
							b=button("Back",20,10,60,30,green,br_green,"back")
							if b==1:
								return
							clock.tick(3) 
						return

		for event in pg.event.get():
			if event.type==pg.QUIT:
				running=False  

		pg.display.update()
	pg.quit()
	return

def start():
	run=True
	while run:
		pg.time.delay(50)
		win.fill(black)
		win.blit(surf,(0,0))
		myfont = pg.font.SysFont('Arial',40,bold=True) #opening image display

		for event in pg.event.get():   #quit on clicking X
			if event.type==pg.QUIT:
				run=False

		textsurface = myfont.render("CONNECT 4", False, (255,215,0))
		win.blit(textsurface,(250,273))
		button("START!",145,635,100,40,green,br_green,"play")
		button("EXIT",485,635,100,40,red,br_red,"quit")

		keys=pg.key.get_pressed()
		pg.display.update()
	pg.quit()

def main():
	c[:]=[5]*7
	a.fill(0)
	start()

if __name__ == "__main__":
    main()










