def solution(n):    
    bigger = n + 1
    n_cnt1 = str(bin(n)).count('1')

    while True:
        b_cnt1 = str(bin(bigger)).count('1')
        
        if n_cnt1 == b_cnt1:
            break
        bigger += 1

    return bigger