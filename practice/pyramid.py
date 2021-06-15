
rows = int(input("enter the number of rows: "))

for i in reversed(range(rows)):
    for j in range(1,i+2):
        print(j, end="")
    print('\r')    


