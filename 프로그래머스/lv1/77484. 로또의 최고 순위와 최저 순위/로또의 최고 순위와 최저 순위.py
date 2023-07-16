def solution(lottos, win_nums):
    correct_num = 0
    zero_num = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
    
    for num in lottos:
        if num in win_nums:
            correct_num += 1
            
    worst = rank[correct_num]
    best = rank[correct_num + zero_num]
    return [best, worst]