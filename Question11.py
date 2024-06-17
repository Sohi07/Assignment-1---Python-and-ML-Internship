def fibonacci_sequence(n):

    sequence = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci_sequence(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")
