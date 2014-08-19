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
  if left_side != 'wall':
    
    while touch() != 'wall':
      move()
  elif right_side != 'wall':
    
     while touch() != 'wall':
      move()
  