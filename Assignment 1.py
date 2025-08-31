# Function to perform Insertion Sort in monotonically decreasing order
def insertion_sort_decreasing(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are smaller than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at the correct position
        arr[j + 1] = key

# Test the function with an example array
if __name__ == "__main__":
    # Example array to be sorted in monotonically decreasing order
    test_array = [12, 11, 13, 5, 6]
    
    print("Original Array:", test_array)
    
    # Calling the function to sort the array
    insertion_sort_decreasing(test_array)
    
    # Print the sorted array
    print("Sorted Array in Decreasing Order:", test_array)
