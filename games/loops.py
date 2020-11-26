
for i in range(1,10):
    if i == 1:
        print(" "*20, end="")
        print(i)

    z = 0
    for j in range(10-i):
        print(" ", end=" ")

    for j in range(i):
        print(j+1, end=" ")
        z+=1
    for x in range(z, -1, -1):
        print(x+1, end=" ")

    print()



