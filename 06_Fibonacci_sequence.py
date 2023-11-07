def fibonacci(n):
    fib = []

    previous1 = 1
    previous2 = 1

    fib.append(previous1)
    fib.append(previous2)

    for i in range(2, n):
        new = previous1 + previous2
        fib.append(new)

        previous1 = previous2
        previous2 = new
    
    return fib

n = int(input("Enter the number of terms in the sequence: "))
fib = fibonacci(n)
print(fib)