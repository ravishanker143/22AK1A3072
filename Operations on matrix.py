import numpy as np

def add_matrices(A, B):
    """Add two matrices."""
    return np.add(A, B)

def subtract_matrices(A, B):
    """Subtract two matrices."""
    return np.subtract(A, B)

def multiply_matrices(A, B):
    """Multiply two matrices."""
    return np.dot(A, B)

def trace_matrix(A):
    """Calculate the trace of a matrix."""
    return np.trace(A)

# Get the dimensions of the matrices from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create two matrices
A = np.zeros((rows, cols))
B = np.zeros((rows, cols))

# Get the elements of the matrices from the user
print("Enter elements of matrix A:")
for i in range(rows):
    for j in range(cols):
        A[i, j] = float(input(f"Enter element [{i+1}, {j+1}]: "))

print("Enter elements of matrix B:")
for i in range(rows):
    for j in range(cols):
        B[i, j] = float(input(f"Enter element [{i+1}, {j+1}]: "))

# Perform operations
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)

print("Addition:")
print(add_matrices(A, B))

print("Subtraction:")
print(subtract_matrices(A, B))

print("Multiplication:")
print(multiply_matrices(A, B))

print("Trace of Matrix A:")
print(trace_matrix(A))

print("Trace of Matrix B:")
print(trace_matrix(B))