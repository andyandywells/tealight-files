from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 
  for i in range(0, edges):
    move(size)
    turn(angle)
    
polygon(400,2.5)