def isAscending(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def isDecending(lst):
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            return False
    return True

def isAllSame(lst):
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            return False
    return True

def hasDupe(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False
    

def somethingDrome(lst):
    if isAllSame(lst):
        return "Repdrome"
    elif isAscending(lst):
        if hasDupe(lst):
            return "Plaindrome"
        return "Metadrome"
    elif isDecending(lst):
        if hasDupe(lst):
            return "Nialpdrome"
        return "Katadrome"
    else:
        return "Nondrome"





inp = [int(i) for i in input("Enter Input : ")]
print(somethingDrome(inp))