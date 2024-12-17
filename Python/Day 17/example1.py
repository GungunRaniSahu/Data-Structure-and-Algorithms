#Fibonacci Series with Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
print([fibonacci_recursive(i) for i in range(n)])
