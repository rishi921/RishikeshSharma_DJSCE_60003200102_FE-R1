def steal(nums):
    odds = 0
    even = 0

    for i in range(0, len(nums)):
        if i % 2 == 0:
            even += nums[i]
        else:
            odds += nums[i]

    if len(nums) % 2 == 0:
        return max(odds, even)
    else:
        return max(odds, even - min(nums[0], nums[-1]))
             
            
print(steal([2,3,2]))
print(steal([1,2,3,1]))
print(steal([1,2,3]))