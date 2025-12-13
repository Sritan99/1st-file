
import pgzrun
import random

WIDTH=700
HEIGHT=700

a=Actor("alien")
b=Actor("alien_2")

message=" "

def draw(): 
 screen.fill("blue")
 a.draw() 
 b.draw()
 screen.draw.text(message,center=(300,300),fontsize=30)

def on_mouse_down(pos):
 global message
 if a.collidepoint(pos) or b.collidepoint(pos):
  message="Good shot"
  rand()

 else:
  message="You missed"

def rand():
 a.x=random.randint(0,500)
 a.y=random.randint(0,500)
 
 b.x=random.randint(0,500)
 b.y=random.randint(0,500)

 

 













pgzrun.go()