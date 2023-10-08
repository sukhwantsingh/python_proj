def binary_search(arr, target):
    """
    Perform binary search to find the target element in a sorted list.
    
    Args:
    arr (list): The sorted list in which to search.
    target: The element to search for.
    
    Returns:
    int: The index of the target element in the list, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index.

        if arr[mid] == target:
            return mid  # Target found, return the index.

        elif arr[mid] < target:
            left = mid + 1  # Adjust the left boundary.

        else:
            right = mid - 1  # Adjust the right boundary.

    return -1  # Target not found in the list.

# Example usage:
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target_element = 7
    result = binary_search(sorted_list, target_element)

    if result != -1:
        print(f"{target_element} found at index {result}.")
    else:
        print(f"{target_element} not found in the list.")
