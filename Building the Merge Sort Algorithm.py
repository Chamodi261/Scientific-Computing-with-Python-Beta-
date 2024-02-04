def merge_sort(array):
    """
    Perform merge sort on the given array in-place.

    Parameters:
    - array (list): The list of elements to be sorted.

    Returns:
    None (The array is sorted in-place).
    """
    # Base case: If the array has one or zero elements, it is already sorted
    if len(array) <= 1:
        return
    
    # Divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort the left and right halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Merge the sorted left and right halves
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from the left half
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Copy any remaining elements from the right half
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    
    # Perform merge sort on the array
    merge_sort(numbers)
    
    print('Sorted array: ' + str(numbers))
