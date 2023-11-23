def solution(numbers, hand):
    answer = ''
    numbers = list(map(str, numbers))
    coordinate = {'1': (1, 1), '2': (1, 2), '3': (1, 3), '4': (2, 1), '5': (2, 2), '6': (2, 3), '7': (3, 1),
                  '8': (3, 2), '9': (3, 3), '*': (4, 1), '0': (4, 2), '#': (4, 3)}

    leftThumbNow = coordinate['*']
    rightThumbNow = coordinate['#']

    for number in numbers:
        targetLocation = coordinate[number]
        if number in ['1', '4', '7', '*']:
            answer += 'L'
            leftThumbNow = targetLocation
        elif number in ['3', '6', '9', '#']:
            answer += 'R'
            rightThumbNow = targetLocation
        else:
            closerThumb = find_closer_thumb(leftThumbNow, rightThumbNow, targetLocation)
            if closerThumb == 'same':
                if hand == 'left':
                    answer += 'L'
                    leftThumbNow = targetLocation
                else:
                    answer += 'R'
                    rightThumbNow = targetLocation
                continue
            elif closerThumb == 'L':
                leftThumbNow = targetLocation
            else:
                rightThumbNow = targetLocation
            answer += closerThumb

    return answer


def find_closer_thumb(left, right, target):
    leftDistance = abs(left[0] - target[0]) + abs(left[1] - target[1])
    rightDistance = abs(right[0] - target[0]) + abs(right[1] - target[1])
    if leftDistance > rightDistance:
        return 'R'
    elif leftDistance < rightDistance:
        return 'L'
    return 'same'
