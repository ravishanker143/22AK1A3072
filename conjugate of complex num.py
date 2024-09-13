# Get the complex numbers from the user
real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
c1 = complex(real1, imag1)

real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))
c2 = complex(real2, imag2)

# Perform operations
add = c1 + c2
sub = c1 - c2
mul = c1 * c2
conj_c1 = c1.conjugate()
conj_c2 = c2.conjugate()

# Print the results
print("Complex Number 1:", c1)
print("Complex Number 2:", c2)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Conjugate of Complex Number 1:", conj_c1)
print("Conjugate of Complex Number 2:", conj_c2)