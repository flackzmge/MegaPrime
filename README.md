# MegaPrime


Use the following functions:

## is_prime(n)

This function takes a positive integer n as input and returns True if n is a prime number, and False otherwise.

## is_megaprime(n)

This function takes a positive integer n as input and returns True if n is a megaprime, and False otherwise. A megaprime is a prime number that contains only prime digits. For example, the number 23 is a megaprime because it is a prime number and its digits 2 and 3 are both prime.

## megaprime(max)

This function takes a positive integer max as input and returns a list of all megaprimes less than or equal to max.

# Examples
```
# Check if a number is prime
print(is_prime(5))  # Output: True
print(is_prime(12))  # Output: False

# Check if a number is a megaprime
print(is_megaprime(23))  # Output: True
print(is_megaprime(22))  # Output: False

# Find all megaprimes less than or equal to a number
print(megaprime(100))  # Output: [2, 3, 5, 23, 29, 31, 37, 53, 59, 71, 73, 79]
```
