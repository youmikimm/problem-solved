def solution(players, callings):
    rankDict = {name: rank for rank, name in enumerate(players)}   # 선수: 순위
        
    for name in callings:
        rank = rankDict[name]
        rankDict[name] -= 1
        rankDict[players[rank-1]] += 1
        players[rank-1], players[rank] = players[rank], players[rank-1]
        
    return players