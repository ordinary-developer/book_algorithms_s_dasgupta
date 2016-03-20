def fibonacci(n):
    """
    returns the n-th member of a fibonacci sequence
    (an exponential algorithm)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(fibonacci(3))
