
num_rows, num_cols = map(int, input("Enter the number of rows and columns separated by a space: ").split())

matrix = []
for _ in range(num_rows):
    row = list(map(int, input("Enter row elements separated by a space: ").split()))
    matrix.append(row)
print("Matrix:")
for row in matrix:
    print(row)
