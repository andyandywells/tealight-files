from tealight.logo import move, turn, color

colors = ["black", "green", "blue"]


for i in range(0,100):
  move(i)
  turn(90)
  color(colors[i%3])