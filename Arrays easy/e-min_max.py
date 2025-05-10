#Min and max of array:
#Given an array arr. Your task is to find the minimum and maximum elements in the array. Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

def get_min_max(arr):
    min_val = float('inf')
    max_val = float('-inf')
    for i in range (len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
        if max_val < arr[i]:
            max_val = arr[i]
    return min_val,max_val
arr = [3, 2, 1, 56, 10000, 167]
print(get_min_max(arr))