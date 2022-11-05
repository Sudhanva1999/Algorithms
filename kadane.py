# Max possible contigous sub array sum
def getMaxSubArraySum(inputArray):
    maxSum = -999999
    currentSum = 0
    for num in inputArray:
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    
    return maxSum 

inputArray = map(int, list(input("Enter array to get max possible contigous sub array sum:\n").split()))
print("Max possible contigous sub array sum is: " + str(getMaxSubArraySum(inputArray)))
