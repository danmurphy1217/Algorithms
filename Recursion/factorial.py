def fact(n):
    """factorial recursive function example."""
    if n <= 1:
        return 1
    else:
        return n*fact(n - 1)

if __name__ == '__main__':
    print(fact(10))
    print(fact(1))
    print(fact(0))
