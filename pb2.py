
def fibonacci_sum(max):
    fib1 = 1
    fib2 = 2
    sum = 0
    while fib2 < max:
        if fib2%2 == 0:
            sum +=fib2
        temp = fib1
        fib1 = fib2
        fib2 = temp + fib1
    return sum

print fibonacci_sum(4000000)
