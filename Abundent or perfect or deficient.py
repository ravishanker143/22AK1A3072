def sum_of_divisors(n):
    """Calculate the sum of divisors of a number."""
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def classify_number(n):
    """Classify a number as abundant, perfect, or deficient."""
    sum_divisors = sum_of_divisors(n)
    if sum_divisors > n:
        return "Abundant"
    elif sum_divisors == n:
        return "Perfect"
    else:
        return "Deficient"

num = int(input("Enter a number: "))

result = classify_number(num)

print(f"The number {num} is {result}.")