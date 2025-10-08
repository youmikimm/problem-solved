def solution(sizes):
    answer = 0
    width_list = []
    height_list = []
    
    for i in range(len(sizes)):
        sizes[i].sort()
        width_list.append(sizes[i][0])
        height_list.append(sizes[i][1])
        
    return max(width_list) * max(height_list)