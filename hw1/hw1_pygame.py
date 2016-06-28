import pygame
import os
pygame.init()

width=600
height=400

green=(0,120,0)

gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("Jizz In Pangfeng")
clock=pygame.time.Clock()
crashed=False
pangfengIMG=pygame.image.load(os.path.join(os.path.dirname(__file__),'pangfeng.png'))
jizzIMG=pygame.image.load(os.path.join(os.path.dirname(__file__),'jizz.png'))

class jizz:
	def __init__(self,x,y):
	    self.x=x
	    self.y=y

def pangfeng_move(x,y):
    gameDisplay.blit(pangfengIMG,(x,y))

arr=[]
def jizz_mov(pos):
    gameDisplay.blit(jizzIMG,(pos.x,pos.y))
def jizzz():
    for i in range(len(arr)-1,0,-1):
        arr[i].y-=4
        if arr[i].y<-50:
            arr.remove(arr[i])
        else:
            jizz_mov(arr[i])
def newjizzz(x,y):
    arr.append(jizz(x,y))
x=width*0.5-45
y=height-150

UP=False
DOWN=False
LEFT=False
RIGHT=False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed=True
        print(event)

        if event.type == pygame.KEYDOWN and event.key==273: UP=True
        if event.type == pygame.KEYDOWN and event.key==274:	DOWN=True
        if event.type == pygame.KEYDOWN and event.key==276: LEFT=True
        if event.type == pygame.KEYDOWN and event.key==275: RIGHT=True

        if event.type == pygame.KEYUP and event.key==273:   UP=False
        if event.type == pygame.KEYUP and event.key==274:   DOWN=False
        if event.type == pygame.KEYUP and event.key==276:   LEFT=False
        if event.type == pygame.KEYUP and event.key==275:   RIGHT=False

        if event.type == pygame.KEYDOWN and event.key==32:   newjizzz(x+20,y-50)
        
    if UP : y-=2
    if DOWN : y+=2
    if LEFT : x-=2
    if RIGHT : x+=2

    gameDisplay.fill(green)
    jizzz()
    pangfeng_move(x,y)

    pygame.display.update()
    clock.tick(120)
pygame.quit()
print("123")