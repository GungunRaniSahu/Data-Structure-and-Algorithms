#Fibonacci Series with Memoization
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

n = 10
print([fibonacci_memo(i) for i in range(n)])
