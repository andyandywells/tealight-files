from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

print "This is art mode!"

print screen_width
print screen_height

background("paper.jpg")

line(0,0,screen_width, screen_height)

spot(200,300, 20)

circle(300,200, 20)

box(500, 500, 60, 60)

image(200,200,"bird.png")

line(560,0,560,495)

text(100, 100, "Hello Tealight!")

lastx = None
lasty = None
hue = 0

def handle_mousemove(x,y):
  global lastx, lasty, hue
  
  image(lastx or x, lasty or y, x, y)
 
  
  
  
  lastx = x
  lasty = y
  
