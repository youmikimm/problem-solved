import Foundation

func solution(_ money:Int) -> [Int] {
    let coffee = 5500
    return [money / coffee, money % coffee]
}