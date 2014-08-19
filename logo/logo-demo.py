from tealight.logo import (move, 
                           turn,
                           color)

print "This is tealight!"

colors = ["red", "blue", "green"]

for i in range(10,10,100):
  move(i)
  turn(83)
  c = colors[(i / 5)%3]
  color(c)
