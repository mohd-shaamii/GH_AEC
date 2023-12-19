def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Example: Print the first 10 numbers in the Fibonacci series
n = 10
result = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci series are: {result}")
