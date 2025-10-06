from collections import defaultdict

def solution(gems):
    answer_set = set(gems)
    total_count = len(answer_set) # 보석의 총 개수
    s = 0
    e = 0
    answer = [0, len(gems) - 1]
    gem_count = defaultdict(int)
    gem_count[gems[0]] = 1

    while s < len(gems) and e < len(gems):
        if len(gem_count) == total_count:
            if (e - s) < (answer[1] - answer[0]): # 최소구간 갱신
                answer = [s, e]

            gem_count[gems[s]] -= 1
            if gem_count[gems[s]] == 0:
                del gem_count[gems[s]]
            s += 1
        else:
            e += 1
            if e == len(gems):
                break
            gem_count[gems[e]] += 1

    return [answer[0] + 1, answer[1] + 1]