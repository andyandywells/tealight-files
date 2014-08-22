
def initialiseMatrix():
  matrix = [[0 for i in range(7)] for j in range(7)]
  matrix[2][1] = 1
  matrix[3][2] = 1
  matrix[4][3] = 1
  matrix[5][4] = 1
  print(matrix)
  return matrix
  

matrix = initialiseMatrix()


#check diagonal from left to right
def checkDiagonalLR():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+2][col+2] and matrix[row][col] == matrix[row+3][col+3]:
         return True
      else:
        return False
      

#check diagonal from right to left
def checkDiagonalRL():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row-1][col+1] and matrix[row][col] == matrix[row-2][col+2] and matrix[row][col] == matrix[row-3][col+3]:
        print("four in a row")
      else:
        return False

#check horizontal 
def checkHorizontal():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+2][col] and matrix[row][col] == matrix[row+3][col]:
        print("four in a row")
      else:
        return False

#check vertical
def checkVertical():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row][col-1] and matrix[row][col] == matrix[row][col-2] and matrix[row][col] == matrix[row][col-3]:
        print("four in a row")
      else:
        return False

def checkWin():
  checkVertical()
  checkHorizontal()
  checkDiagonalRL()
  checkDiagonalLR()


   
checkWin()