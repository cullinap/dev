
def ubbi_dubbi():
    word  = input("enter a word: ")
    chars = []

    for c in word:
        if c in 'aeiou':
            chars.append(f'ub{c}')
        else:
            chars.append(c)

    return ''.join(chars)        

def main():
    print(ubbi_dubbi())

main()
