def solution(people, limit):
    boat = 0
    people.sort()
    max_idx = len(people) - 1
    min_idx = 0

    while max_idx >= min_idx:
        if max_idx == min_idx:
            boat += 1
            break
        
        if people[max_idx] + people[min_idx] > limit:
            max_idx -= 1
        else:
            max_idx -= 1
            min_idx += 1
            
        boat += 1
    return boat