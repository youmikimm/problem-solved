func solution(_ x:Int) -> Bool {
    var dString = String(x)
    var divider: Int = 0
    
    for c in dString {
        if let num = c.wholeNumberValue {
            divider += num
        }
    }
    
    return (x % divider == 0)
}