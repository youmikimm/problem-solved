def solution(dirs):
    directions = list(dirs)
    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    trackSet = set()
    x, y = 0, 0
    
    for d in directions:
        newX = x + moves[d][0]
        newY = y + moves[d][1]
        
        if abs(newX) > 5 or abs(newY) > 5:
            continue
        
        trackSet.add((x, y, newX, newY))
        trackSet.add((newX, newY, x, y))
        x = newX
        y = newY
    
    return len(trackSet) // 2