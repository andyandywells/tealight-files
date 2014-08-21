def initialiseMatrix():
  matrix = [[0 for i in range(7)] for j in range(7)]
  return matrix

matrix = initialiseMatrix()

def checkwin():
  for row in range(0,6):
    for col in range (0,6):
      if ( matrix[row][col] == 1 and ((matrix[row][col] == matrix[row][col-1] and matrix[row][col] == matrix[row][col-2] and matrix[row][col] == matrix[row][col-3])
                                      or (matrix[row][col] == 1 and matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+2][col] and matrix[row][col] == matrix[row+3][col])
                                      or (matrix[row][col] == 1 and matrix[row][col] == matrix[row-1][col+1] and matrix[row][col] == matrix[row-2][col+2] and matrix[row][col] == matrix[row-3][col+3])
                                      or (matrix[row][col] == 1 and matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+2][col+2] and matrix[row][col] == matrix[row+3][col+3]))):
        return 1
        
      else:
        return 0