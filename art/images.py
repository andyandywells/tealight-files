from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 100

width = 5
height = 5

for i in range(0,width):
  for j in range(0,height):
    if j == 1 or 2 or 3 or 4 or 5 and i == 1 or 2 or 3 or 4 or 5:
      image(x + i * 30, y + j * 60, "misc/YellowFlower.png")
    else:
      image(x + i * 30, y + j * 60, "misc/Clover.png")
     
