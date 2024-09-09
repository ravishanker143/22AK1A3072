def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def next_palindrome(n):
    """Find the next palindrome number."""
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    """Check if a number is palindrome."""
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
    print("Next palindrome number:", next_palindrome(num))
else:
    print("Not prime")