from tealight.logo import (move, 
                           turn,
                           color)

print "This is tealight!"

colors = ["red", "blue", "green"]

for i in range(20,10,5):
  move(i)
  turn(83)
  c = colors[(i / 5)%3]
  color(c)
