def solution(board, moves):
    boom = 0
    verticalStacks = [[]]
    basket = []
    
    for j in range(len(board[0])):
        tmp = []
        for i in range(len(board) - 1, -1, -1):
            if board[i][j] != 0:
                tmp.append(board[i][j])
        verticalStacks.append(tmp)
        
    for location in moves:        
        if len(verticalStacks[location]) == 0:
            continue
        doll = verticalStacks[location].pop()
        if len(basket) != 0 and basket[-1] == doll:
            boom += 1
            basket.pop()
            continue
        basket.append(doll)

    return boom * 2