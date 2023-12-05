def removeDuplicates(arr):
    d = {}
    for i in arr:
        d[i] = 1
    
    print(list(d.keys()))
    return len(d.keys())
    
print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))