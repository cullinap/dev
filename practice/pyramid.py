
char = 65

for i in range(5):
    for j in range(i+1):
        print(chr(char), end='')
    char += 1
    print("\r")


