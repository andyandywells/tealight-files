
def initialiseMatrix():
  matrix = [[0 for i in range(7)] for j in range(7)]
  print(matrix)
  return matrix
  

matrix = initialiseMatrix()


#check diagonal from left to right
def checkDiagonalLR():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+2][col+2] and matrix[row][col] == matrix[row+3][col+3]:
         return 1
      else:
        return 0
      

#check diagonal from right to left
def checkDiagonalRL():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row-1][col+1] and matrix[row][col] == matrix[row-2][col+2] and matrix[row][col] == matrix[row-3][col+3]:
        return 1
      else:
        return 0

#check horizontal 
def checkHorizontal():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+2][col] and matrix[row][col] == matrix[row+3][col]:
        return 0
      else:
        return 1

#check vertical
def checkVertical():
  for row in range(0,6):
    for col in range (0,6):
      if matrix[row][col] == 1 and matrix[row][col] == matrix[row][col-1] and matrix[row][col] == matrix[row][col-2] and matrix[row][col] == matrix[row][col-3]:
        return 1
      else:
        return 0

def checkWin():
  checkVertical()
  checkHorizontal()
  checkDiagonalRL()
  checkDiagonalLR()
  if checkHorizontal() == True or checkVertical() == True or checkDiagonalLR() == True or checkDiagonalRL() == True:
    print("four in a row")

initialiseMatrix()    
checkWin()