

def brackets(string):
    open_symbols = ['(', '[', '{']
    close_symbols = [')', ']', '}']
    symbols = []
    for char in string:
        if char in open_symbols:
            symbols.append(char)
        elif char in close_symbols:
            index = close_symbols.index(char)
            if len(symbols) > 0 and symbols[-1] == open_symbols[index]:
                del symbols[-1]
            else:
                return False

    if len(symbols) == 0:
        return True
    else:
        return False
