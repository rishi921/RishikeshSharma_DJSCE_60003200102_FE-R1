def binSearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        
        # print(arr[mid], high, low)
        
        if x == arr[mid]:
            return mid

        elif (arr[mid]) > x:
            high = mid - 1
        else:
            low = mid + 1

    return low
    
print(binSearch([1, 3, 5, 6], 2))
print(binSearch([1, 3, 5, 6], 7))
print(binSearch([1, 3, 5, 6], 0))