import sys
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
values.sort()

start_idx = 0
end_idx = n - 1
answer = [0, 0]
n_sum = sys.maxsize

while start_idx < end_idx:
    start_val = values[start_idx]
    end_val = values[end_idx]
    tmp_sum = start_val + end_val

    if abs(tmp_sum) < n_sum:
        n_sum = abs(tmp_sum)
        answer = [start_val, end_val]
        if n_sum == 0:
            break

    if tmp_sum < 0:
        start_idx += 1
    else:
        end_idx -= 1

print(answer[0], answer[1])