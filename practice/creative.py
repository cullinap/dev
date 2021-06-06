
def pyramid(i,j):
    
    if i == 0:
       return  

    print(''.join(["*" for x in range(j - i)]))
    pyramid(i-1,j)


pyramid(5,6)    
