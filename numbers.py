#numbers in python
#types of number data types in python
#1. int: used to represent whole numbers (e.g., 1, 2
#2. float: used to represent decimal numbers (e.g., 3.14, 2.5)
#3. complex: used to represent complex numbers (e.g., 2 + 3j)
#4. bool: used to represent boolean values (True or False)
x = 5
print(x)
y = 3.14
print(y)
#Complex number
z = 2 + 3j
print(z)
#Boolean values
is_true = True
print(is_true)
#Arithmetic operations
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b)  # Floor division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
#Augmented assignment operators
x = 5
x += 2  # Equivalent to x = x + 2
print(x)
x -= 3  # Equivalent to x = x - 3
print(x)
x *= 4  # Equivalent to x = x * 4
print(x)
x /= 2  # Equivalent to x = x / 2
print(x)
x //= 3  # Equivalent to x = x // 3
print(x)
x %= 2  # Equivalent to x = x % 2
print(x)
x **= 3  # Equivalent to x = x ** 3
print(x)
#Type conversion
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print(num_int)
num_float = float(num_str)  # Convert string to float
print(num_float)
num_str2 = str(num_int)  # Convert integer back to string
print(num_str2)
#Mathematical functions
import math
print(math.sqrt(16))  # Square root
print(math.pow(2, 3))  # Power
print(math.sin(math.pi / 2))  # Sine of 90 degrees
print(math.cos(0))  # Cosine of 0 degrees
print(math.tan(math.pi / 4))  # Tangent of 45 degrees
#Random numbers
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.uniform(0, 1))  # Random float between 0 and 1
#Rounding numbers
num = 3.14159
print(round(num, 2))  # Round to 2 decimal places
print(round(num))  # Round to nearest integer
#Comparing numbers
num1 = 10
num2 = 20
print(num1 > num2)  # Greater than
print(num1 < num2)  # Less than
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not equal to
print(num1 >= num2)  # Greater than or equal to
print(num1 <= num2)  # Less than or equal to
#Math constants
print(math.pi)  # Pi constant
print(math.e)  # Euler's number
#Number formatting
num = 1234567.89
print(f"{num:,.2f}")  # Format with commas and 2 decimal places
#Number formatting with scientific notation
print(f"{num:.2e}")  # Format in scientific notation with 2 decimal places
#Number formatting with percentage
print(f"{num:.2%}")  # Format as percentage with 2 decimal places
#Number formatting with hexadecimal, octal, and binary
print(f"{num_int:x}")  # Format as hexadecimal
print(f"{num_int:o}")  # Format as octal
print(f"{num_int:b}")  # Format as binary
#Number formatting with leading zeros
print(f"{num_int:05d}")  # Format with leading zeros to a width of 5
#Number formatting with alignment
print(f"{num_int:<10d}")  # Left-align within a width of 10
print(f"{num_int:>10d}")  # Right-align within a width of 10
#Number formatting with center alignment
print(f"{num_int:^10d}")  # Center-align within a width of 10
#Number formatting with custom fill character
print(f"{num_int:*^10d}")  # Center-align with '*' as fill character within a width of 10
#Number formatting with sign
print(f"{num_int:+d}")  # Always show sign
print(f"{num_int:d}")  # Show sign only for negative numbers
#Number formatting with parentheses for negative numbers
print(f"{num_int:(d)}")  # Show negative numbers in parentheses
#Number formatting with space for positive numbers
print(f"{num_int: d}")  # Show space for positive numbers and '-' for negative numbers
#Number formatting with zero padding
print(f"{num_int:0>10d}")  # Pad with zeros on the left