#!/usr/bin/env python3

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(str(a))    # see below
        a, b = b, a+b
    return " ".join(result[1:])

print(fib2(55))
print(fib2(100))