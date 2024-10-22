def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # initialize the left and right pointers

    while left <= right:  # loop until pointers converge
        mid = left + (right - left) // 2  # dividing the elements in 2 halves calculating middle index

        if arr[mid] == target:  # compares with inputted target
            return mid  # if target found return the index
        elif arr[mid] < target:  # if not found at mid search the right half
            left = mid + 1  # move left pointer to the right half
        else:  # if not found on right search the left half
            right = mid - 1  # move right pointer to the left half

    return -1  # if target not found return -1

# example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # sample array of sorted elements
target = 7  # target element to search for
result = binary_search(arr, target)  # calling the binary search function

if result != -1:  # if target is found print the result
    print(f"Element found at index {result}")  # output the index of the target element
else:  # if target is not found
    print("Element not found")  # output not found message
