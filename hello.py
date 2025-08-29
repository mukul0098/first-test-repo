#Armstrong Number script


# Armstrong number checker

# Take input from user
num = int(input("Enter a number: "))

# Convert number to string to count digits
order = len(str(num))

# Compute sum of digits raised to the power
sum_of_powers = sum(int(digit) ** order for digit in str(num))

# Check condition
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
