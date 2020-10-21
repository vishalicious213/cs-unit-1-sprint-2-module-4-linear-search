
"""
Rewrite the implementation of linear search below so that the algorithm searches from the end of the list to the beginning.
"""
def linear_search(arr, target):
    # loop through each item in the input array
    for idx in range(len(arr)-1, -1, -1):
        # print(arr[idx])
        # check if the item at the current index is equal to the target
        if arr[idx] == target:
            # return the current index as the match
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1


test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(linear_search(test_arr, 13))