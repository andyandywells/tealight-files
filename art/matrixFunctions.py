

def initialiseMatrix():
  matrix = [[0 for i in range(8)] for j in range(8)]
  return matrix

def checkwin(matrix):
  for row in range(0,7):
    for col in range (0,7):
      if (matrix[row][col] == 1 and ((matrix[row][col] == matrix[row][col-1] and matrix[row][col] == matrix[row][col-2] and matrix[row][col] == matrix[row][col-3])
                                      or (matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+2][col] and matrix[row][col] == matrix[row+3][col])
                                      or (matrix[row][col] == matrix[row-1][col+1] and matrix[row][col] == matrix[row-2][col+2] and matrix[row][col] == matrix[row-3][col+3])
                                      or (matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+2][col+2] and matrix[row][col] == matrix[row+3][col+3]))):
        return True
      elif (matrix[row][col] == -1 and ((matrix[row][col] == matrix[row][col-1] and matrix[row][col] == matrix[row][col-2] and matrix[row][col] == matrix[row][col-3])
                                      or (matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+2][col] and matrix[row][col] == matrix[row+3][col])
                                      or (matrix[row][col] == matrix[row-1][col+1] and matrix[row][col] == matrix[row-2][col+2] and matrix[row][col] == matrix[row-3][col+3])
                                      or (matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+2][col+2] and matrix[row][col] == matrix[row+3][col+3]))):
        return False
