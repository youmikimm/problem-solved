import sys
input = sys.stdin.readline

students = [x for x in range(1, 31)]

for i in range(28):
    students.remove(int(input()))
    
for x in students:
    print(x)