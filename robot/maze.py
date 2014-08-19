from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

while touch() != 'wall':
    move()



while touch() == 'wall':
  if touch() == 'wall':
    turn(1)
  elif left_side () == 'wall':
    turn(1)
  else:
    turn(-1)
  while touch() != 'wall':
      move()
