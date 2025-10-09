def solution(s):
    stack = []
    
    if s[0] == ')':
        return False
    
    for p in s:
        if len(stack) == 0 and p == ')':
            return False
        
        if p == '(':
            stack.append(p)
        elif p == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False