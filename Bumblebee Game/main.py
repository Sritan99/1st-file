import pgzrun
import random


WIDTH=500
HEIGHT=500

bee=Actor("bee")
flower=Actor("flower")


bee.pos=(random.randint(0,400),random.randint(0,400))
flower.pos=(random.randint(0,600),random.randint(0,600))


def draw(): 
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+ str(score), center=(60,20), fontsize=30)

score=0

def update():
    global score
    if keyboard.left:
      bee.x=bee.x-3

    if keyboard.right:
      bee.x=bee.x+3

    if keyboard.up:
      bee.y=bee.y-3

    if keyboard.down:
      bee.y=bee.y+3 
 
    if bee.colliderect(flower):
       
       score=score+1
       rand()
       
        

def rand():
   flower.x=random.randint(40,450)
   flower.y=random.randint(40,450)
 





def time_up():
  
  

clock.schedule_interval(time_up,5)






pgzrun.go()
