from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,700):
  move(i)
  turn(91)
  color(colors[i%3])