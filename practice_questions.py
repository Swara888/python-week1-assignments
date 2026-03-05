import math

# 1. Area of Circle
radius = float(input("Enter radius of circle: "))
area = math.pi * radius * radius
print("Area of circle:", area)

# 2. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter number for factorial: "))
print("Factorial:", factorial(n))

# 4. Count vowels and consonants
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
v = 0
c = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)

# 5. Fibonacci sequence
terms = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci sequence:")

for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
