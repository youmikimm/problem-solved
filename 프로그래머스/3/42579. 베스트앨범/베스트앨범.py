from collections import Counter, defaultdict
def solution(genres, plays):
    answer = []
    best_genres = defaultdict(int)
    best_genres_list = []
    plays_info = defaultdict(list)
    
    for i in range(len(genres)):
        best_genres[genres[i]] += plays[i]
    
    # [(장르1, 재생수1), (장르2, 재생수2), ...]
    best_genres_list = sorted(best_genres.items(), key=lambda x:x[1], reverse=True)
    print(best_genres_list)
    
    idx = 0
    for (genre, play) in zip(genres, plays):
        plays_info[genre].append((play, idx))
        idx += 1
    
    for k in plays_info:
        plays_info[k] = sorted(plays_info[k], key=lambda x:x[0], reverse=True)
    
    for i in best_genres_list:
        count_list = plays_info[i[0]] # 각 곡의 (재생수, 고유번호)
        for i in range(2):
            answer.append(count_list[i][1])
            if len(count_list) == 1:
                break

    return answer