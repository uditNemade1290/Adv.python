# Experiment No. 4
# Efficient Fibonacci using Memoization
def fib(n, memo={}):
    if n in memo:
        return memo[n]  # Return cached result

    if n <= 1:
        return n

    # Calculate and save result
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


# Main program
n = int(input("Enter the value of n: "))

result = fib(n)

print("The Fibonacci number at position", n, "is:", result)
