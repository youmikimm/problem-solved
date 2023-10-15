from itertools import product

def solution(users, emoticons):
    result = []
    for sale_permutation in product([10, 20, 30, 40], repeat=len(emoticons)):
        total_em_plus = 0
        total_amount = 0
        for user in users:  # 사용자별
            em_plus = 0
            amount = 0
            for i in range(len(emoticons)): # 이모티콘별
                if user[0] <= sale_permutation[i]:  # 할인율 크므로 구매
                    amount += emoticons[i] * (1 - sale_permutation[i] / 100)
            if amount >= user[1]: # 계획한 구매 비용을 초과하면 플러스 가입
                amount = 0
                em_plus += 1
            total_em_plus += em_plus
            total_amount += amount
            result.append([total_em_plus, total_amount])
    
    result.sort(key=lambda x : (-x[0], -x[1]))
    return result[0]