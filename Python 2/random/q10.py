# Write a program to generate the Fibonacci sequence up to n terms using dynamic programming (memoization).

def fibo(n):
    if n==0 :
        return 0

    if n==1:
        return 1
    
    return fibo(n-1) + fibo(n-2)

print(fibo(5))
    