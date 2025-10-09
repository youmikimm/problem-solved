def solution(s):
    paren_list = list(s)
    stack = []
    
    if paren_list[0] == ')':
        return False
    
    for p in paren_list:
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