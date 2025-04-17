import sys
import time

sys.setrecursionlimit(10000000)
sys.set_int_max_str_digits(1000000)

def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def load_integers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return [int(x) for x in data.split(',') if x.strip().isdigit()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except ValueError:
        print("Error: File contains non-integer values")
        return []


file_path = 'fibonacciInput.txt'
sample_data = load_integers_from_file(file_path)
memo = {}
for i in range(len(sample_data)):
    start_time = time.time()
    result = fibonacci(sample_data[i], memo)
    end_time = time.time()
    print(f"Result for {sample_data[i]}th term: {result}")
    print(f"Execution time for {sample_data[i]}th term: {end_time - start_time:.6f} seconds")


# n = 10000  # Change this value to test with different inputs
# memo = {}
# start_time = time.time()
# result = fibonacci(n, memo)
# end_time = time.time()
# print(f"Result: {result}")
# print(f"Execution time: {end_time - start_time:.3f} seconds")