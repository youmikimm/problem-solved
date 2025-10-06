import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
cnt = 0

for index in range(n):
    start = 0
    end = n - 1
    while start < end:
        if lst[start] + lst[end] == lst[index]:
            if start != index and end != index:
                cnt += 1
                break
            elif start == index:
                start += 1
            else:
                end -= 1
        elif lst[start] + lst[end] < lst[index]:
            start += 1
        else:
            end -= 1
            
print(cnt)