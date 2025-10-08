from collections import defaultdict

def solution(participant, completion):
    dict = defaultdict(int)
    for n1 in participant:
        dict[n1] += 1
        
    for n2 in completion:
        dict[n2] -= 1
    
    for n3 in dict:
        if dict[n3] == 1:
            return n3