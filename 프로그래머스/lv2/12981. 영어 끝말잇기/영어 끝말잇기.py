def solution(n, words):
    wordsSet = {words[0]}
    
    for i in range(1, len(words)):
        num = i % n + 1
        turn = i // n + 1
        
        if words[i-1][-1] != words[i][0] or words[i] in wordsSet:
            return [num, turn]
        
        wordsSet.add(words[i])
        
    return [0, 0]
