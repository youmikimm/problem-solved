def solution(a, b):
    dayString = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    daysByMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    firstDay = [1] * 13 # 월의 개념 없이 날짜를 누적 -> 각 월의 첫째날
    for i in range(2, 13):
        firstDay[i] = firstDay[i-1] + daysByMonth[i-1]
    
    calculatedDay = firstDay[a] + b - 1 # 주어진 날을 누적으로 구한 값
    
    return dayString[calculatedDay % 7 - 1]