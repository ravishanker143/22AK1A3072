def is_fibonacci(n):
    a, b = 0, 1
    position = 1
    while b < n:
        a, b = b, a + b
        position += 1
    return b == n, position

# Test the function
num = 21
is_fib, position = is_fibonacci(num)
if is_fib:
    print(f"{num} is a Fibonacci number at position {position}")
else:
    print(f"{num} is not a Fibonacci number")


