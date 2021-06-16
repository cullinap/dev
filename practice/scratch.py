
nums = [2,7,11,15]
target = 9

table = {}

for i in range(len(nums)):
    complement = target - nums[i]
    if complement in table.keys():
        secondIndex = nums.index(complement)
        if i != secondIndex:
            print(sorted([i,secondIndex]))
    table.update({nums[i]:i})        


