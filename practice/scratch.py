
n = 3 


def stairs():
    if n <= 2:
        return n

    res, step_1, step_2 = 0,1,2
    for i in range(2,n):
        res = step_2 + step_1
        step_1 = step_2
        step_2 = res
    return res    

print(stairs())
