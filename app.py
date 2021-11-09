#! /usr/bin/env python3

# This function needs only one argument: an array.
def merge_sort(arr):
    # This function works only if the length of the array
    # is greater than 1. If the array is not greater than 1,
    # the array is already sorted and no further action is 
    # needed.
    if len(arr) > 1:
        # Let's define the recursive part of the algorithm.
        # We need to define two sub-arrays: one that goes
        # from the beginning of the original array to the
        # middle point.
        left_arr = arr[:len(arr)//2] # // = rounding off to the next int
        # And one that goes from the middle point to the end
        # of the original array.
        right_arr = arr[len(arr)//2:]
        
        # Time to call mergesort recursively on both arrays.
        # After running these two lines, both left and right
        # array will be in sorted order.
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        # Implementing the merge step. Here, we want to compare
        # the left most element of one array to the left most
        # element of the other array.
        # i will keep track of the most left element of the left
        # array.
        i = 0
        # j will keep track of the most left element of the right
        # array.
        j = 0
        # We'll use a third variable to keep track of the index in
        # the merged array.
        k = 0
        
        # Using a while loop to compare the left array at index i
        # with the right array at index j.
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                # When we see that the left array is smaller than
                # the right array at the current indexes, we'll
                # save the value of the left array inside our
                # merged array.
                arr[k] = left_arr[i]
                # Then, we have to increase i.
                i += 1
            else:
                # If the right array at index j is smaller than the
                # left array OR ARE EQUAL, we do the same thing,
                # but we save the right array in the merged array
                # instead.
                arr[k] = right_arr[j]
                # And again, we increase j.
                j+= 1
            # And we increase k (outside of the loop, because it
            # will be increased in either case).
            k += 1
        
        # Now we have to consider the possibility of having looked
        # into every element of the right array and having transferred
        # every element from the right array to the merged array.
        # There's nothing to compare the left elements with. Therefore,
        # we just consider the case that we want to transfer every
        # element from the left array to the merged array while not
        # considering the right array.
        
        # In this case, i is still smaller than the length of the
        # left array, because there are still elements missing from
        # the left array to be transfered to the merged array.
        while i < len(left_arr):
            # We transfer them by assigning the left array at index i,
            # to the merged array at index k.
            arr[k] = left_arr[i]
            # And afterwards, increasing both indexes.
            i += 1
            k += 1
        
        # Similarly, if there are no more elements in the left array
        # to compare the elements of the array with, we transfer them to
        # the merged array.
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Testing by defining a test array
arr = [22, 11, 88, 66, 55, 77, 33, 44, 88]
print(f"Original array: {arr}")
# Calling mergesort on the array above
merge_sort(arr)
print(f"Sorted array: {arr}")
print()

# Testing one more time
another_arr = [11, 100, 3, 23, 91, 200, 17]
print(f"Original array: {another_arr}")
merge_sort(another_arr)
print(f"Sorted array: {another_arr}")
