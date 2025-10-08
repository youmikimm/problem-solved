from itertools import product
def solution(word):
    alphabet = ['A','E','I','O','U']
    word_list = []
    
    for i in range(1, 6):
        for x in product(alphabet, repeat=i):
            word_list.append(''.join(x))
    
    word_list.sort()
    
    return word_list.index(word) + 1