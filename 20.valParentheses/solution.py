def isValid(s: str) -> bool:
    stack = []
    
    if(len(s) == 0):
        return True
    elif(len(s) % 2 != 0):
        return False
    elif(s[0] == ')' or s[0] == ']' or s[0]=='}'):
            return False
    for symbol in s:
        if(symbol == '(' or symbol == '{' or symbol == '['):
            stack.append(symbol)
        elif(symbol == ')' and len(stack) != 0):
            if(stack[-1] != '('):
                return False
            else:
                stack.pop()
        elif(symbol == '}' and len(stack) != 0):
            if(stack[-1] != '{'):
                return False
            else:
                stack.pop()   
        elif(symbol == ']'):
            if(stack[-1] != '['):
                return False
            else:
                stack.pop()       
    if(len(stack) != 0):
        return False
    else:
        return True
    
def main():
    Input1 = "()"
    assert(isValid(Input1) == True)

    Input2 = "()[]{}"
    assert(isValid(Input2) == True)

    Input3 = "(]"
    assert(isValid(Input3) == False)

    Input4 = "([)]"
    assert(isValid(Input4) == False)

    Input5 = "{[]}"
    assert(isValid(Input5) == True)

main()