import pgzrun
import random

WIDTH=700
HEIGHT=700

bee=Actor("bee")
flower=Actor("flower")


bee.pos=(random.randint(0,600),random.randint(0,600))
flower.pos=(random.randint(0,600),random.randint(0,600))

def draw(): 
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()


def update():
    if keyboard.left:
      bee.x=bee.x-3

    if keyboard.right:
      bee.x=bee.x+3

    if keyboard.up:
      bee.y=bee.y-3

    if keyboard.down:
      bee.y=bee.y+3 

pgzrun.go()






pgzrun.go()