def solution(brown, yellow):
    total = yellow + brown
    
    for i in range(3, int(total ** 0.5) + 1):
        height = i
        width = total // i
        if (height - 2) * (width - 2) == yellow:
            return [width, height]