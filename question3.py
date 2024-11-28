"""
 * Name: Nolan
 * Student ID: 1113543
 * Date of Submission: 11/28/2024
 *
 * Program to combine multiple sorted arrays into a single sorted array using a Min-Heap.
 * Features:
 * 1. Push the first element of each array into the Min-Heap.
 * 2. Remove the smallest element, add it to the merged array, and insert the next element from the same array.
 * 3. Repeat until all arrays are fully processed.
"""

import heapq

def merge_sorted_lists(lists):
    # Create a min-heap to store elements
    priority_queue = []
    merged_result = []

    # Push the first element of each list into the heap
    for list_index, lst in enumerate(lists):
        if lst:  # Ensure the list is not empty
            heapq.heappush(priority_queue, (lst[0], list_index, 0))  # (value, list_index, element_index)

    # Process the heap to generate the merged sorted list
    while priority_queue:
        value, list_index, element_index = heapq.heappop(priority_queue)
        merged_result.append(value)  # Add the smallest element to the merged result
        next_index = element_index + 1

        # If there are more elements in the current list, add the next element to the heap
        if next_index < len(lists[list_index]):
            heapq.heappush(priority_queue, (lists[list_index][next_index], list_index, next_index))

    return merged_result

# Input handling
num_lists = int(input("Enter the number of sorted lists: "))
sorted_lists = [list(map(int, input().split())) for _ in range(num_lists)]

# Merge the sorted lists
final_merged_list = merge_sorted_lists(sorted_lists)

# Print the result
print("Merged Array:", final_merged_list)
