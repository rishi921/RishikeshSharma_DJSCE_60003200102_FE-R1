def profitEarn(prices):
    maxArray = []
    for i in prices[::-1]:
        if len(maxArray) == 0:
            maxArray.append(i)
        else:
            maxArray.append(max(maxArray[-1], i))
    
    m = 0
    # print(maxArray)

    maxArray = maxArray[::-1]
    for i in range(len(prices)):
        m = max(m, maxArray[i]-prices[i]) 

    return m
    
print(profitEarn([7,1,5,3,6,4]))
print(profitEarn([1,1,1,1,1]))
print(profitEarn([1,2,3,4,5]))