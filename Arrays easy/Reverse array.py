#Reverse Array
def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while j >= i:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return arr
arr = [3, 2, 1, 56, 10000, 167]
print(reverseArray(arr))