# Get the input array from the user
arr = list(map(int, input("Enter an array of integers (separated by spaces): ").split()))

# Initialize the minimum difference and the corresponding pair
min_diff = float('inf')
pair = ()

# Iterate over each pair of elements in the array
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        # Calculate the sum of the current pair
        pair_sum = arr[i] + arr[j]
        # Calculate the absolute difference between the sum and zero
        diff = abs(pair_sum)
        # If the difference is less than the current minimum difference, update the minimum difference and the corresponding pair
        if diff < min_diff:
            min_diff = diff
            pair = (arr[i], arr[j])

# Print the result
print("Pair with sum nearest to zero:")
print(pair)