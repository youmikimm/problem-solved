def solution(want, number, discount):
    wantIndex = {want[i] : i for i in range(len(want))}
    possibleDays = 0
    
    for i in range(len(discount) - 9):
        dList = discount[i:i+10]
        numberTmp = number.copy()
        
        for thing in dList:
            if thing in want and numberTmp[wantIndex[thing]] > 0:
                numberTmp[wantIndex[thing]] -= 1
            
        if all(num <= 0 for num in numberTmp):
            possibleDays += 1
    return possibleDays