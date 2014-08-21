global matrix
def initialiseMatrix():
  matrix = [[0 for i in range(7)] for j in range(7)]
  matrix[0][0] = 1
  matrix[1][1] = 1
  matrix[2][2] = 1
  matrix[3][3] = 1
  
  
  print(matrix)
  print(len(matrix))
  return matrix


matrix = initialiseMatrix()
#check diagonal from left to right
def checkDiagonalLR():
  for col in range(0,6):
    for row in range (0,6):
      if matrix[col][row] == 1 and matrix[col][row] == matrix[col+1][row+1] and matrix[col][row] == matrix[col+2][row+2] and matrix[col][row] == matrix[col+3][row+3]:
        print("four in a row")
      

#check diagonal from right to left
def checkDiagonalRL():
  for col in range(6,0):
    for row in range (6,0):
      if matrix[col][row] == 1 and matrix[col][row] == matrix[col-1][row-1] and matrix[col][row] == matrix[col-2][row-2] and matrix[col][row] == matrix[col-3][row-3]:
        print("four in a row")


checkDiagonalRl()