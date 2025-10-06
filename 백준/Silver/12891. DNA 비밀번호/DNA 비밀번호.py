import sys
from collections import defaultdict
input = sys.stdin.readline

total_len, pw_len = map(int, input().split())
DNA = list(input().strip())
cnt_array = list(map(int, input().split())) # 비밀번호에 포함되어야 하는 A C G T의 개수

s = 0
e = s + pw_len - 1
count = 0 # 만들 수 있는 비밀번호 가짓수

current_cnt = defaultdict(int)
for k in ['A','C','G','T']:
    current_cnt[k] = 0

for k in DNA[s:e+1]:
    current_cnt[k] += 1

while True:
    if current_cnt['A'] >= cnt_array[0] \
            and current_cnt['C'] >= cnt_array[1] \
            and current_cnt['G'] >= cnt_array[2] \
            and current_cnt['T'] >= cnt_array[3]:
        count += 1

    e += 1
    if e == total_len:
        break
    current_cnt[DNA[e]] += 1
    current_cnt[DNA[s]] -= 1
    s += 1

print(count)