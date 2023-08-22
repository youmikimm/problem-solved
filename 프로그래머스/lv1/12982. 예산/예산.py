def solution(d, budget):
    cnts = []
    d.sort()
    
    for amount in d:
        if amount <= budget:
            budget -= amount
            cnts.append(amount)
    
    return len(cnts)