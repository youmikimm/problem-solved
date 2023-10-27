str = input()
answer = ''

for s in str:
    if ord(s) >= 97:    # 소문자
        answer += s.upper()
    else:
        answer += s.lower()
        
print(answer)