# Majority Voting Algorithm to find element occuring
# more than n/2 times in an array of length n
def getMajorityElement(nums):
    candidate = nums[0]
    votes = 0
    for num in nums:
        if(num == candidate):
            votes += 1 
        else:
            votes -= 1 

        if(votes == 0):
            candidate = num
            votes = 1

    return candidate

print(getMajorityElement([2,2,4,4,2,2,4,4,4,5,5,5,5,5,5,5,5,5,4,4]))

