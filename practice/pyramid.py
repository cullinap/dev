
def pyramid():
    row = int(input("enter the number of rows: "))
    
    letter = 65 

    for i in range(row):
        for j in range(i+1):
            print(chr(letter), end=" ")
        letter += 1 
        print("\r")    

pyramid()
