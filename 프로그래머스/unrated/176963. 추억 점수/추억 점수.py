def solution(name, yearning, photo):
    answer = []
    
    for eachPhoto in photo:
        photoSum = 0
        for person in eachPhoto:
            if person in name:
                photoSum += yearning[name.index(person)]
        answer.append(photoSum)
    return answer