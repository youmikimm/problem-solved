import sys
input = sys.stdin.readline

light = {
    "0": "1110111",
    "1": "0010010",
    "2": "1011101",
    "3": "1011011",
    "4": "0111010",
    "5": "1101011",
    "6": "1101111",
    "7": "1110010",
    "8": "1111111",
    "9": "1111011",
    " ": "0000000"
}

t = int(input())
for _ in range(t):
    a, b = input().split()
    a = a.rjust(5, " ")
    b = b.rjust(5, " ")
    clicks = 0
    for i in range(5):
        if a[i] == b[i]:
            continue
        else:
            for j in range(7):
                if light[a[i]][j] != light[b[i]][j]:
                    clicks += 1
    print(clicks)