import random

matrix = [[random.randint(0, 9) for i in range(9)] for j in range(9)]

arr_line = []
l = len(matrix)
n = 0  # сдвиг обхода

i = int(l / 2)
j = int(l / 2)

arr_line.append(matrix[i][j])
while True:
    n += 1
    for k in range(n):
        i -= 1
        arr_line.append(matrix[i][j])
    if n == l:
        break
    for k in range(n):
        j += 1
        arr_line.append(matrix[i][j])
    n += 1
    for k in range(n):
        i += 1
        arr_line.append(matrix[i][j])
    for k in range(n):
        j -= 1
        arr_line.append(matrix[i][j])

for mat in matrix:
    print(mat)
print(*arr_line)
