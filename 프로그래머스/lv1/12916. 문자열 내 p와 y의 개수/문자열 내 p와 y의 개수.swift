import Foundation

func solution(_ s:String) -> Bool
{
    var pCnt = 0
    var yCnt = 0
    
    for ch in s {
        if ch == "p" || ch == "P" {
            pCnt += 1
        } else if ch == "y" || ch == "Y"{
            yCnt += 1
        }
    }

    return pCnt == yCnt
}