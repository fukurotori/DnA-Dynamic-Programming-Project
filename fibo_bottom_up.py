import sys
import time

sys.setrecursionlimit(2000)
sys.set_int_max_str_digits(1000000)

def fibonacci_bottom_up(n, fib_table):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Fill the table in a bottom-up manner
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

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
    fib_table = [0] * (sample_data[i] + 1)
    if sample_data[i] != 0:
        fib_table[1] = 1
    start_time = time.time()
    result = fibonacci_bottom_up(sample_data[i], fib_table)
    end_time = time.time()
    print(f"Result for {sample_data[i]}th term: {result}")
    print(f"Execution time for {sample_data[i]}th term: {end_time - start_time:.6f} seconds")


# n = 1000000  # Change this value to test with other inputs
# fib_table = [0] * (n + 1)
# fib_table[1] = 1
# start_time = time.time()
# result = fibonacci_bottom_up(n, fib_table)
# end_time = time.time()

# print(f"Result: {result}")
# print(f"Execution time: {end_time - start_time:.3f} seconds")