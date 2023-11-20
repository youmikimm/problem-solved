import sys
input = sys.stdin.readline

scores_num = int(input())
difficulty = list(map(int, input().split()))
questions = int(input())
mistakes = [0]

tmp_mistake = 0
for i in range(scores_num-1):
    if difficulty[i] > difficulty[i+1]:
        tmp_mistake += 1
    mistakes.append(tmp_mistake)

for _ in range(questions):
    start, end = map(int, input().split())
    print(mistakes[end-1] - mistakes[start-1])