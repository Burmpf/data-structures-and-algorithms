from data_structures.hashtable import Hashtable
import re 

def first_repeated_word(string):
    words = re.findall(r'\w+', string)
    hashtable = Hashtable()
    for word in words:
        if hashtable.has(word):
            return word
        else:
            hashtable.set(word, word)
    return None