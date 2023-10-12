def solution(want, number, discount):
    possibleDays = 0
    wishCart = []
    for i in range(len(want)):
        wishCart.extend([want[i]] * number[i])
    wishCart.sort()
        
    for i in range(len(discount) - 9):
        dList = discount[i:i+10]
        dList.sort()
        
        if wishCart == dList:
            possibleDays += 1
    
    return possibleDays