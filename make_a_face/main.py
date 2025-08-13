from p5 import *

screen_size = 400


def setup():
    # Put code to run once here
    size(screen_size, screen_size)
    rect_mode(CENTER)


def draw():
    # Put code to run every frame here
    background(255, 255, 255)
    #Add code to draw your face here
    # wajah
    fill(0,0,0)
    no_stroke()
    ellipse(200,215,200,200)
    fill(164,159,196)
    ellipse(153,230,107,140)
    ellipse(246,230,107,140)
    ellipse(200,255,176,130)
    # mata
    fill(0,0,0)
    ellipse(235,235,27,27)
    ellipse(160,235,27,27)
    fill(255,255,255)
    ellipse(240,230, 10,10)
    ellipse(165,230,10,10)
    fill(164,159,196)
    ellipse(235,255,30,30)
    ellipse(160,255,30,30)
    # mulut
    fill(0,0,0)
    rect(200,260,60,4)
    triangle(220, 260, 230, 260, 225, 290)
    triangle(190, 260, 210, 260, 225, 290)

    
   
    
        



# Keep this to run your code
run()
