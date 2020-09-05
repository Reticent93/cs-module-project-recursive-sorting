# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # Your code here
    left = right = 0
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    if left < len(arrA):
        merged_arr.extend(arrA[left:])
    if right < len(arrB):
        merged_arr.extend(arrB[right:])

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left, right = merge_sort(arr[0:len(arr) // 2]), merge_sort(arr[len(arr) // 2:])
        return merge(left, right)
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
