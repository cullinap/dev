
def pigLatin(sentence):
    
    if sentence[0] in 'aeiou':
        return f'{sentence}way'

    return f'{sentence[1:]}{sentence[0]}way'    

def pl_sentence():
    
    sentence = input("enter a sentence: ")

    translatedSentence = []
    for w in sentence.split():
        translatedSentence.append(pigLatin(w))

    return ' '.join(translatedSentence)    


def print_pl():
    print(pl_sentence())

print_pl()    


