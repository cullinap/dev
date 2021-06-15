
nums = [2,7,11,15]
target = 9
hashTable = {}


for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashTable.keys():
        secondIndex = nums.index(complement)
        if i != secondIndex:
            print(sorted([i,secondIndex]))
    hashTable.update({nums[i]:i})        






