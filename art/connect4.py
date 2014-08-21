def initialiseMatrix():
  matrix = [[0 for i in range(7)] for j in range(7)]
  matrix[0][0] = 1
  matrix[1][1] = 1
  matrix[2][2] = 1
  matrix[3][3] = 1
  print(matrix)

initialiseMatrix()

print(len(matrix))