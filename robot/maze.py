from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def movement():
  for n in range(0, 10):
   if touch() !== 'wall':
      move()