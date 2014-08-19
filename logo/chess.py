from tealight.logo import move, turn, color

colors = ["black", "red"]


def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
    
for i in range(0,1):
  
  turn(180)
  
  for i in range(0,8):
      polygon(4,250)
      move(10)
