import sys
input = sys.stdin.readline

N = int(input())
x = []
y = []
for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

x.append(x[0])    # 처음 점을 마지막에 또 추가
y.append(y[0])

result = 0
    
def triangle(x1, y1, x2, y2):    # 원점과 두 점이 이루는 삼각형의 넓이(ccw)
    return (x1*y2 - x2*y1) / 2

for i in range(N):
    result += triangle(x[i], y[i], x[i+1], y[i+1])
    
print(round(abs(result), 1))