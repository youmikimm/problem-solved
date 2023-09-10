func solution(_ seoul:[String]) -> String {
    if let idx = seoul.firstIndex(of: "Kim") {
        return "김서방은 \(idx)에 있다"
    }
    return "wrong"
}