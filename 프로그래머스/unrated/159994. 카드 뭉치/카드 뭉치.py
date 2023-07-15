def solution(cards1, cards2, goal):
    
    for x in goal:
        if len(cards1) > 0 and x == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and x == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
            
    return "Yes"