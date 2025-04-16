def fibonacci_bottom_up(n, fib_table):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Fill the table in a bottom-up manner
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

# Example usage
if __name__ == "__main__":
    n = 10  # Change this value to test with other inputs
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    print(f"Fibonacci number at position {n} is {fibonacci_bottom_up(n, fib_table)}")