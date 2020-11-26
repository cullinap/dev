
for i in range(10):
    if i < 10:

        for j in range(10-i):
            print(" ", end=" ")

        for j in range(1,i+1):
            print(j, end=" ")

        for j in range(i-1, 0, -1):
            print(j, end=" ")

    print()





