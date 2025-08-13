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
    fill(60,170,190)
    no_stroke()
    ellipse(200,220,200,200)
    fill(190, 60, 62)
    rect(200,215,170,35)
    fill(190, 60, 62)
    ellipse(280,215,40,40)
    fill(190, 60, 62)
    ellipse(120,215,40,40)
    fill(0,0,0)
    ellipse(235,215,27,27)
    ellipse(160,215,27,27)
    fill(0,0,0)
    ellipse(235,215,27,27)
    ellipse(160,215,27,27)
    
   
    
        



# Keep this to run your code
run()
