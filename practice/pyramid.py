
rows = int(input("enter the number of rows: "))

for i in reversed(range(rows + 1)):
    for j in range(i):
        print("* ", end="")
    print('\r')    

