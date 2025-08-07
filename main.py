from p5 import *
from random import randint

def mouse_pressed():
    # print("🎯")
    if hit_colour == Color("blue").hex:
        print("you hit the outer circle, 50 points!")
    elif hit_colour == Color("red").hex:
        print("you hit the inner circle, 200 points!")
    else:
        print("you missed, no points!")
    
def shoot_arrow():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour) 
    fill("brown")
    circle(arrow_x, arrow_y, 15)
    
def setup():
    size(400, 400)
    no_stroke()
    
def draw():
    fill("cyan")
    rect(0, 0, 400, 250)
    fill("lightgreen")
    rect(0, 250, 400, 150)
    fill("brown")
    triangle(150, 350, 200, 150, 250, 350)
    fill("blue")
    circle(200, 200, 170)
    fill("red")
    circle(200,200,110)
    fill("yellow")
    circle(200, 200, 30)
    shoot_arrow()
 
run(frame_rate=2)

