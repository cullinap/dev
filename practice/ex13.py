from collections import Counter


def most_repeating_word(words):
    return max(words, key=lambda x: Counter(x).most_common(1)[0][1])

WORDS = ['this','is','an','elementary','test','example']
print(most_repeating_word(WORDS))
