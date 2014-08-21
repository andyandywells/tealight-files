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

for i in range(0,6):
  for j in range (0,6):
    if matrix[i] == matrix [j+1]:
      print("two in a row")
  