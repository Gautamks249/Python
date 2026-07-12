# Functions  
# Write a function factorial(n) that returns the factorial of a number using recursion.

def fact(n):
    if n==0 or n==1 : return 1
    return n*fact(n-1)

n = int(input("Enter a number : "))
print(f"Factorial of {n} = {fact(n)}")
