def findMinDiff(arr,M):
    arr = sorted(arr)
    min_diff = float('inf')
    end = len(arr) - M
    i = 0
    while i <= end:
        curr_diff = arr[i+M-1] - arr[i]
        min_diff = min(min_diff,curr_diff)
        i += 1
    return min_diff
arr = [7, 3, 2, 4, 9, 12, 56]
m = 5
print(findMinDiff(arr,m))