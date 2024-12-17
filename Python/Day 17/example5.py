#Fibonacci Numbers Modulo
def fibonacci_mod(n, mod):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod
    return b

n = 10
mod = 1000000007
print([fibonacci_mod(i, mod) for i in range(n)])
