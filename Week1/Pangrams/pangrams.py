def pangrams(sentence: str):
    new_sentence = sentence.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    alphabet_dict = dict.fromkeys(alphabet, 0)
    if len(new_sentence) <= 1000:
        for i in new_sentence:
            if i in alphabet_dict.keys():
                alphabet_dict[i] += 1
    else:
        return f'Your sentence have much length'
    for value in alphabet_dict.values():
        if value == 0:
            return f'not pangram'
        
    return f'pangram'



print(pangrams('We promptly judged antique ivory buckles for the next prize')) # pangram
#print(pangrams('We promptly judged antique ivory buckles for the prize')) #not pangram

