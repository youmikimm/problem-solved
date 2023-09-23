def solution(s):
    count = 0
    
    for i in range(len(s)):
        paren = s[i:] + s[:i]
        if check(paren):
            count += 1
    return count    
    
    
def check(pString):   # p: String
    if len(pString) % 2 == 1:
        return False
    
    stack = []
    
    for p in pString:
        if p == '[' or p == '(' or p == '{':
            stack.append(p)
        else:
            if len(stack) == 0: # 비어있음
                return False
            if (p == ']' and stack[-1] == '[') or (p == ')' and stack[-1] == '(') or (p == '}' and stack[-1] == '{'):
                    stack.pop()
            else:
                return False
        
    return True     # 짝이 맞음
        