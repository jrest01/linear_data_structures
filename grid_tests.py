from grid import Grid


matrix = Grid(3, 3)
print(matrix)

for row in range(matrix.get_height()):
    for col in range(matrix.get_width()):
        matrix[row][col] = row * col

print(matrix)
print(matrix.get_height())
print(matrix.get_width())
print(matrix.__getitem__(1))
print(matrix.__getitem__(2)[0])
print(matrix.__str__())