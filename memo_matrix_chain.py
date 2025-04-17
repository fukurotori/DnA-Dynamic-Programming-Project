import sys
import time

def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0] * n for _ in range(n)]  # Minimum scalar multiplications
    s = [[0] * n for _ in range(n)]  # Optimal split points

    def memoized_matrix_chain(i, j):
        if m[i][j] != 0:
            return m[i][j]
        if i == j:
            m[i][j] = 0
        else:
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = (memoized_matrix_chain(i, k) +
                     memoized_matrix_chain(k + 1, j) +
                     p[i] * p[k + 1] * p[j + 1])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
        return m[i][j]

    memoized_matrix_chain(0, n - 1)
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i + 1}"
    else:
        return f"({print_optimal_parens(s, i, s[i][j])} x {print_optimal_parens(s, s[i][j] + 1, j)})"

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

# Sample input
# sample_data = [5, 2, 3, 10, 5, 4, 20]
file_path = 'matrixinput.txt'
sample_data = load_integers_from_file(file_path)
n = sample_data[0]
p = sample_data[1:]

if len(p) != n + 1:
    print("Invalid input. The number of dimensions must be n+1.")

else:
    start_time = time.time()
    m, s = matrix_chain_order(p)
        

    optimal_cost = m[0][n - 1]
    optimal_parens = print_optimal_parens(s, 0, n - 1)
    end_time = time.time()
    time_taken = end_time - start_time

    print("Optimal number of scalar multiplications:", optimal_cost)
    print("Optimal parenthesization:", optimal_parens)
    print("Time taken (seconds):", time_taken)
