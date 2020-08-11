# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #binary search algorith is supposed to work with ordered arrays

    #Base case
    #The start point is greater or equal to the end point
    if end >= start:
        #delcare a middle point
        middle = (start + end) // 2
    
        #if the tagget is present at the middle,
        #return middle
        if arr[middle] == target:
            return middle
    
        #if the target is smaller than the middle
        #then it's in the left subarray
        elif arr[middle] > target:
            #recurse
            return binary_search(arr, target, start, middle - 1) #elimanate RHS
        
        #if the target is greater or equal to the middle
        #it's in the right subarray
        else:
            return binary_search(arr, target, middle +1, end) #eliminate LHS
    else:
        return -1 #target not found





# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

