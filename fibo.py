import sys
import time

sys.setrecursionlimit(2000)

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

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
for i in range(len(sample_data)):
    start_time = time.time()
    result = fibonacci(sample_data[i])
    end_time = time.time()
    print(f"Result for {sample_data[i]}th term: {result}")
    print(f"Execution time for {sample_data[i]}th term: {end_time - start_time:.3f} seconds")

# result = fibonacci(53)
# print(f"Result: {result}")
# print(f"Execution time: {end_time - start_time:.3f} seconds")