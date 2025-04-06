#include<iostream>

#include <unordered_map>

std::unordered_map<int, long long> memo;

long long fibonacci(int n) {
    if (n <= 1) return n;
    if (memo.find(n) != memo.end()) return memo[n];
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
    return memo[n];
}

int main() {
    int n;
    std::cout << "Enter the value of n: ";
    std::cin >> n;
    std::cout << "Fibonacci(" << n << ") = " << fibonacci(n) << std::endl;
    return 0;
}