

def polindrom(text):
    return text == text[::-1]


def anagram(a, b):
    return Counter(a) == Counter(b)




from collections import Counter