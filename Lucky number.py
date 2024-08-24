def calculate_lucky_number(day, month, year):
    lucky_number = day + month + year
    while lucky_number > 9:
        lucky_number = sum(int(digit) for digit in str(lucky_number))
    return lucky_number

# Test the function
day = int(input("Enter your day of birth (1-31): "))
month = int(input("Enter your month of birth (1-12): "))
year = int(input("Enter your year of birth (4 digits): "))
lucky_number = calculate_lucky_number(day, month, year)
print(f"Your lucky number is {lucky_number}")
