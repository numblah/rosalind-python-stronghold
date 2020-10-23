def Fibonacci_loop_pythonic (months, offspring):
    parent, child = 1, 1
    for itr in range(months-1):
        child, parent = parent, parent +(child*offspring)
    return child


print(Fibonacci_loop_pythonic(36,4))