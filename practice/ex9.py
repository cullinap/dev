import snoop

def firstLast(seq):
    return seq[:1] + seq[-1:]


#@snoop
def even_odd_sums(seq):
    evens = 0
    odds = 0

    #return seq[:1]

    for i in range(len(seq)):
        if i % 2 == 0:
            evens += seq[i:i+1][0] 
        else:
            odds += seq[i:i+1][0] 
    
    return [evens, odds]

#print(firstLast([10,20,30,40,50,60]))
print(even_odd_sums([10,20,30,40,50,60]))
print(even_odd_sums((10,20,30,40,50,60)))

