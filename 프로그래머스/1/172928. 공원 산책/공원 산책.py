def solution(park, routes):
    currentPoint = find_init_loc(park)
    parkEnd = (len(park)-1, len(park[0])-1)    # (verticalEnd, horizontalEnd)

    for r in routes:
        order = route_to_int(r)
        if not pass_condition1(order, currentPoint, parkEnd):
            continue
        if not pass_condition2(order, currentPoint, park):
            continue
        currentPoint = update_location(order, currentPoint)

    return currentPoint


def find_init_loc(park):
    for i in range(len(park)):
        if 'S' in park[i]:
            return [i, park[i].find('S')]


def route_to_int(route):
    order = []
    routeList = route.split(' ')
    if routeList[0] == 'E':
        order = [0, int(routeList[1])]
    elif routeList[0] == 'W':
        order = [0, -int(routeList[1])]
    elif routeList[0] == 'S':
        order = [int(routeList[1]), 0]
    elif routeList[0] == 'N':
        order = [-int(routeList[1]), 0]

    return order


def pass_condition1(order, current, parkEndIdx):   # 공원을 벗어나면 False
    nextLoc = [order[i] + current[i] for i in range(2)]

    if nextLoc[0] < 0 or nextLoc[1] < 0 or nextLoc[0] > parkEndIdx[0] or nextLoc[1] > parkEndIdx[1]:
        return False
        
    return True


def pass_condition2(order, current, park):   # 장애물을 만나면 False
    nowY = current[0]
    nowX = current[1]

    nextY = nowY + order[0]
    nextX = nowX + order[1]

    if nowY == nextY:  # 가로 방향 이동, nowX < nextX이도록 보정
        if nowX > nextX:
            nowX, nextX = nextX, nowX
        if 'X' in park[nowY][nowX+1: nextX+1]:
            return False
    
    if nowY > nextY:  # 세로 방향 이동 시, nowY < nextY이도록 보정
        nowY, nextY = nextY, nowY
        
    for i in range(nowY, nextY+1):
        if park[i][nowX] == 'X':
            return False
            
    return True


def update_location(order, current):
    nextLoc = [order[i] + current[i] for i in range(2)]
    return nextLoc
