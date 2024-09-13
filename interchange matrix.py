# Get the input matrix from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} (separated by spaces): ").split()))
    matrix.append(row)

# Interchange the first and last column
for row in matrix:
    row[0], row[-1] = row[-1], row[0]

# Print the modified matrix
print("Modified Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))