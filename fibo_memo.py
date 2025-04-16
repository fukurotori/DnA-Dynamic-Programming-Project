import sys

sys.setrecursionlimit(2000)

def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


n = 1000  # Change this value to test with different inputs
memo = {}
print(f"Fibonacci({n}) = {fibonacci(n, memo)}")