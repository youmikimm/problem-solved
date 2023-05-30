import sys
input = sys.stdin.readline
msg = list(input().strip())
key = list(input().strip())
alphabet = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    # J 제외

for i in range(0, len(msg), 2):    # msg 두 글자씩 끊는 처리
    if msg[i] == msg[i+1]:  # 겹치는 문자
        if msg[i] == "X":
            msg.insert(i+1, "Q")
        else:
            msg.insert(i+1, "X")
    if (i+1) == len(msg):   # 메시지가 홀수개라면 끝에 X를 붙임
        msg.append("X")

playfairKey = [[] for x in range(5)]    # 5x5 플레이페어 키 생성
for i in range(5):
    for _ in range(5):
        if len(key) != 0:
            k = key.pop(0)
            playfairKey[i].append(k)
            if k in alphabet:
                alphabet.remove(k)
        else:   # 입력받은 key가 소진됨
            playfairKey[i].append(alphabet.pop(0))

print("".join(msg))
print(playfairKey)