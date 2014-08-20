from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 100

width = 8
height = 8

for i in range(0,width):
  for j in range(0,height):
    if j % 4 == 0:
      image(x + j * 30, y + j * 60, "misc/YellowFlower.png")
    else:
      image(x + i * 30, y + j * 60, "misc/Clover.png")
     
