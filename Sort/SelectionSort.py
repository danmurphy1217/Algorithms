def findSmallestIndex(arr):
    """
    returns the index of the smallest value in an array. First, it sets the
	index of the smallest value to 0 and the smallest value to arr[0]. Then,
	it searches through arr and keeps track of the smallest value and index.
	@params : arr, an array of integers
	@returns: index value of the smallest value
    """
    smallestValueIndex = 0
    smallestValue = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallestValue:
            smallestValue = arr[i]
            smallestValueIndex = i
    return smallestValueIndex


def selectionSort(arr):
    """
    returns the sorted array. Uses findSmallestIndex() at each iteration
    to determine the next smallest index value to pop from the array and
    append to the sorted array.
	@params: arr, an array to sort
	@returns: sorted arr
    """
    sortedArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallestIndex(arr)
        sortedArr.append(arr.pop(smallestIndex))
    return sortedArr
if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))
    print(selectionSort([100, 2, 57, 253, 135, 67, 34, 25, 135, 12]))
    