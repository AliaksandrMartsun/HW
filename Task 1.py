

def brackets(str):
    lst = []
    for i in str:
        if i == '(' or i == '[' or i == '{':
            lst.append(i)
            continue
        if i == ')':
            x = lst.pop()
            if x != '(':
                return False
        elif i == ']':
            x = lst.pop()
            if x != '[':
                return False
        elif i == '}':
            x = lst.pop()
            if x != '{':
                return False
    if len(lst):
        return False
    else:
        return True


a = '([fg]fg)'
print(brackets(a))
