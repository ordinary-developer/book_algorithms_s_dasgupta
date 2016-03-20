def fibonacci(n):
    """
    returns the n-th member of a fibonacci sequence
    (polynomial algorithm)
    """
    if n == 0:
        return 0

    f = [None] * (n + 1)
    f[0] = 0; f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


if __name__ == '__main__':
    print(fibonacci(6))
