def factorial_recur(n):
    if (n == 1):
        return 1
    else:
        return(n * factorial_recur(n - 1))

print(factorial_recur(6))