#Fibonacci Series with Space Optimization
def fibonacci_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 10
print([fibonacci_optimized(i) for i in range(n)])
