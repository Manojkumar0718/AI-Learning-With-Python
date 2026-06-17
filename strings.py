#This file is about strings 
my_string = "Hello, World!"
print(my_string)
#string operations
print(my_string.upper())  # Convert to uppercase
print(my_string.lower())  # Convert to lowercase
print(my_string.replace("World", "Python"))  # Replace substring
print(my_string.split(","))  # Split string into a list
print(len(my_string))  # Get the length of the string

#Check if a substring exists in the string
if "Hello" in my_string:
    print("Substring found!")
if "Python" in my_string:
    print("Substring found!")

#Check if the string starts or ends with a specific substring
if my_string.startswith("Hello"):
    print("String starts with 'Hello'")
if my_string.endswith("!"):
    print("String ends with '!'")

#String formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
#String slicing
sliced_string = my_string[0:5]  # Get the first 5 characters
print(sliced_string)
#forward slicing
forward_sliced_string = my_string[7:12]  # Get characters from index 7 to 11
print(forward_sliced_string)
#backward slicing
backward_sliced_string = my_string[-6:-1]  # Get characters from index -6 to -2
print(backward_sliced_string)
#String concatenation
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ", " + string2 + "!"
print(concatenated_string)
#String methods
print(my_string.count("l"))  # Count occurrences of a substring
print(my_string.find("World"))  # Find the index of a substring
print(my_string.index("World"))  # Find the index of a substring (raises an error if not found)
#String stripping
print(my_string.strip())  # Remove leading and trailing whitespace
print(my_string.lstrip())  # Remove leading whitespace
print(my_string.rstrip())  # Remove trailing whitespace
#String validation
print(my_string.isalpha())  # Check if all characters are alphabetic
print(my_string.isdigit())  # Check if all characters are digits
print(my_string.isalnum())  # Check if all characters are alphanumeric
#String joining
list_of_strings = ["Hello", "World", "from", "Python"]
joined_string = " ".join(list_of_strings)  # Join list of strings with a space
print(joined_string)
#String reversing
reversed_string = my_string[::-1]  # Reverse the string
print(reversed_string)
#String formatting with format()
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string2)
#String formatting with % operator
formatted_string3 = "My name is %s and I am %d years old." % (name, age)
print(formatted_string3)
#String formatting with str.format() and named placeholders
formatted_string4 = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(formatted_string4)
#String formatting with f-strings and expressions
formatted_string5 = f"My name is {name.upper()} and I will be {age + 1} next year."
print(formatted_string5)
#String formatting with f-strings and conditional expressions
formatted_string6 = f"My name is {name} and I am {'an adult' if age >= 18 else 'a minor'}."
print(formatted_string6)
#String formatting with f-strings and loops
names = ["Alice", "Bob", "Charlie"]
for n in names:
    print(f"Hello, {n}!")
#String formatting with f-strings and dictionaries
person = {"name": "Alice", "age": 30}
print(f"My name is {person['name']} and I am {person['age']} years old.")
#String formatting with f-strings and lists
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(f"Number: {n}")
#String formatting with f-strings and tuples
person_tuple = ("Alice", 30)
print(f"My name is {person_tuple[0]} and I am {person_tuple[1]} years old.")
#String formatting with f-strings and sets
unique_numbers = {1, 2, 3, 4, 5}
for n in unique_numbers:
    print(f"Unique number: {n}")
#String formatting with f-strings and nested data structures
nested_data = {"person": {"name": "Alice", "age": 30}, "numbers": [1, 2, 3]}
print(f"My name is {nested_data['person']['name']} and I am {nested_data['person']['age']} years old. My favorite numbers are {nested_data['numbers']}.")   
#String formatting with f-strings and functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
