p1win = "Red wins"
p2win = "Yellow wins"

def initialiseMatrix():
  matrix = [[0 for i in range(7)] for j in range(7)]
  matrix[2][1]
  matrix[3][2]
  matrix[4][3]
  matrix[5][4]
  return matrix

def checkwin():
  for row in range(0,6):
    for col in range (0,6):
      if ( matrix[row][col] == 1 and ((matrix[row][col] == matrix[row][col-1] and matrix[row][col] == matrix[row][col-2] and matrix[row][col] == matrix[row][col-3])
                                      or (matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+2][col] and matrix[row][col] == matrix[row+3][col])
                                      or (matrix[row][col] == matrix[row-1][col+1] and matrix[row][col] == matrix[row-2][col+2] and matrix[row][col] == matrix[row-3][col+3])
                                      or (matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+2][col+2] and matrix[row][col] == matrix[row+3][col+3]))):
        return p1win
      if ( matrix[row][col] == -1 and ((matrix[row][col] == matrix[row][col-1] and matrix[row][col] == matrix[row][col-2] and matrix[row][col] == matrix[row][col-3])
                                      or (matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+2][col] and matrix[row][col] == matrix[row+3][col])
                                      or (matrix[row][col] == matrix[row-1][col+1] and matrix[row][col] == matrix[row-2][col+2] and matrix[row][col] == matrix[row-3][col+3])
                                      or (matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+2][col+2] and matrix[row][col] == matrix[row+3][col+3]))):
        return p2win
      else:
        return 0

checkwin()