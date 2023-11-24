def solution(s):
    s = s[2:-2]
    answer = []
    stringList = s.split('},{')
    numList = stringToTwoDimList(stringList)
    numList.sort(key=len)
    answer.append(numList[0][0])
    
    for i in range(1, len(numList)):
        for j in range(i + 1):
            currentNum = numList[i][j]
            if currentNum not in answer:
                answer.append(currentNum)
                break
    return answer


def stringToTwoDimList(s):
    result = []
    for strWithComma in s:
        splittedList = list(map(int, strWithComma.split(',')))
        result.append(splittedList)
    return result