
def mySum(*items):
    if not items:
        return items 
    output = items[0]
    for item in items[1:]:
        output += item 
    return output    

print(mySum(1,2,3))
print(mySum('abc','def'))
print(mySum([10,20,30],[40,50,60],[70,80]))
print(mySum())        


