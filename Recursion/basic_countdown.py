def countdown(i):
    """basic countdown example."""
    if i == 0:
        return
    else:
        print(i)
        return countdown(i - 1)

if __name__ == '__main__':
    countdown(10)
    countdown(1)
    countdown(0)
