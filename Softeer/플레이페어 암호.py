import sys
import string
input = sys.stdin.readline
plaintext = list(input().strip())
tmp = []   # 조건에 맞게 처리한 평문
key = list(input().strip())     # 입력받은 키
ciphertext = []     # 암호문을 저장할 리스트

alphabet = list(string.ascii_uppercase)
alphabet.remove('J')    # J 제외

def transpose(matrix):  # 배열 전치하는 함수
    rows = len(matrix)
    cols = len(matrix[0])

    # 전치된 배열을 담을 빈 배열 생성
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    # 반복문을 사용하여 전치 수행
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

playfairKey = [[] for x in range(5)]    # 5x5 플레이페어 키 생성
for i in range(5):
    for _ in range(5):
        while True:
            if len(key) > 0:  # 최초 등장한 알파벳
                if key[0] in alphabet:
                    k = key.pop(0)
                    playfairKey[i].append(k)    # playfair key에 추가
                    alphabet.remove(k)
                    break
                else:   # 이미 나왔던 알파벳
                    key.pop(0)
            elif len(key) == 0:  # 입력받은 key가 소진됨
                playfairKey[i].append(alphabet.pop(0))
                break

tpPlayfairKey = transpose(playfairKey)
def isRow(char1, char2):
    global playfairKey
    for i in range(0,len(playfairKey)):
        if char1 in playfairKey[i] and char2 in playfairKey[i]:
            return i
    return -1
def isColumn(char1, char2):
    global playfairKey
    for i in range(0, len(playfairKey)):
        if char1 in tpPlayfairKey[i] and char2 in tpPlayfairKey[i]:
            return i
    return -1

p = 0
while True:    # plaintext 두 글자씩 끊는 처리. i=0,2,4,..
    if p >= len(plaintext):
        break
    if p == len(plaintext) - 1: # 마지막 글자
        tmp.append(plaintext[p])
        break
    if plaintext[p] == plaintext[p+1]:  # 겹치는 문자
        tmp.append(plaintext[p])
        if plaintext[p] == 'X':
            tmp.append('Q')
            plaintext.insert(p + 1, 'Q')
        else:
            tmp.append('X')
            plaintext.insert(p + 1, 'X')
    else:
        tmp.append(plaintext[p])
        tmp.append(plaintext[p+1])
    p += 2
if len(plaintext) % 2 != 0:   # 글자가 홀수개라면 끝에 X 붙이기
    tmp.append('X')

for i in range(0, len(tmp), 2):     # 암호화
    row = isRow(tmp[i], tmp[i+1])
    col = isColumn(tmp[i], tmp[i+1])
    if row != -1:   # 같은 행
        idx1 = playfairKey[row].index(tmp[i])
        idx2 = playfairKey[row].index(tmp[i+1])
        ciphertext.append(playfairKey[row][(idx1 + 1) % 5])
        ciphertext.append(playfairKey[row][(idx2 + 1) % 5])
    elif col != -1:  # 같은 열
        idx1 = tpPlayfairKey[col].index(tmp[i])
        idx2 = tpPlayfairKey[col].index(tmp[i + 1])
        ciphertext.append(tpPlayfairKey[col][(idx1 + 1) % 5])
        ciphertext.append(tpPlayfairKey[col][(idx2 + 1) % 5])
    else:
        idx1 = []
        idx2 = []
        for j in range(0, len(playfairKey)):
            for k in range(0, len(playfairKey[j])):
                if tmp[i] == playfairKey[j][k]:
                    idx1.append(j)
                    idx1.append(k)
                elif tmp[i+1] == playfairKey[j][k]:
                    idx2.append(j)
                    idx2.append(k)
        ciphertext.append(playfairKey[idx1[0]][idx2[1]])
        ciphertext.append(playfairKey[idx2[0]][idx1[1]])

print(''.join(ciphertext))