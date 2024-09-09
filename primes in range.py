# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get the range from the user
from_num = int(input("Enter the starting number: "))
to_num = int(input("Enter the ending number: "))

# Print all prime numbers in the range
for num in range(from_num, to_num + 1):
    if is_prime(num):
        print(num)