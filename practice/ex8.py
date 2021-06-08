
def strsort():
    string = input("Enter a string: ")
    
    return ''.join(sorted(string))

def sortSentence():
    sentence = input("Enter a sentence: ")

    return ', '.join(sorted(sentence.split()))

#print(strsort())
print(sortSentence())
