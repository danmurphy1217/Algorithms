def binary_search(data, item):
    """
    Binary Search Algorithm implemented in Python.
    The binary search algorithm takes a sorted list
    and the item you are searching for as it's input
    and returns the position of the item or null (
        if the item is not in the list
    )
    @params: data, a sorted list to search, and item,
    the item to search for
    @returns: the integer of the item in the sorted
    list or null
    @examples:
    >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8], 7)
    6
    >>> binary_search([2, 10, 12, 22, 300, 540, 692], 10)
    1
    """
    high = len(data) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        prediction = data[mid]
        if prediction == item:
            return mid
        elif prediction > item:
            """
            if prediction is greater than what you are searching for,
            move high to (midpoint-1) and try again
            """
            high = mid - 1
        else:
            """
            if prediction is less than what you are searching for,
            i.e. not greater than the item, move low to (midpoint+1)
            and try again
            """
            low = mid + 1
    return None


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 7))
    print(binary_search([2, 10, 12, 22, 300, 540, 692], 10))
