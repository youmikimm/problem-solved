def find_odd_sum(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total


T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print(f'#{test_case} {find_odd_sum(numbers)}')