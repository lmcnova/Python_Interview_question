# Simple Fibonacci Series Generator Using Iteration in Python
def fibonacci_series(n):
    a, b, = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print(f"Fibonacci series : {fibonacci_series(10)}")


# Using Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print("Using Recursion:", [fibonacci_recursive(i) for i in range(10)])

#  Using a While Loop
def fibonacci_while(n):
    a, b = 0, 1
    seq = []
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return seq

print("Using While Loop:", fibonacci_while(10))


# Using a Generator
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Using Generator:", list(fibonacci_generator(10)))


# Using Built-in Tools (Reduce)
from functools import reduce

def fibonacci_reduce(n):
    return reduce(lambda seq, _: seq + [seq[-1] + seq[-2]], range(n - 2), [0, 1])[:n]

print("Using Built-in Tools:", fibonacci_reduce(10))



