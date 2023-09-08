import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer: [Int] = []
    
    for i in 0 ..< commands.count {
        let sIdx = commands[i][0] - 1
        let eIdx = commands[i][1] - 1
        let loc = commands[i][2] - 1

        var sortedArr = array[sIdx...eIdx].sorted()
        answer.append(sortedArr[loc])
    }
    
    return answer
}