from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

def movement():
  while touch() != 'wall':
    move()

if touch() == 'wall':
  if left_side() != 'wall':
    movement()
 else if right_side() != 'wall':
    movement()