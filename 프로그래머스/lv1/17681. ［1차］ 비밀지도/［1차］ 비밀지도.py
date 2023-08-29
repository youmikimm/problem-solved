def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        encodedString = str(bin(arr1[i] | arr2[i]))[2:].rjust(n, '0')
        decodedString = ""
        for j in range(len(encodedString)):
            if encodedString[j] == '0':
                decodedString += " "
            else:
                decodedString += "#"
        answer.append(decodedString)
        
    return answer