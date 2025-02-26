
Matrix = []

for i in range(9):
  Matrix.append(list(map(int, input().split(" "))))

for i in range(9):
  for j in range(9):
    if Matrix[i][j] == max(map(max,Matrix)):
      a = i +1
      b = j +1
print(max(map(max,Matrix)))
print(a,b)