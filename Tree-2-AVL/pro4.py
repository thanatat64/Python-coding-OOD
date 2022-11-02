def getChild(lst,n):
    L_index,R_index = 2*n + 1,2*n + 2
    L = lst[L_index] if L_index < len(lst) else 0
    R = lst[R_index] if R_index < len(lst) else 0
    return L,R

def powerOfKnight(lst,n):
    return lst[n] + sum(getChild(lst,n))

def compareKnight(lst,a,b):
    if powerOfKnight(lst,a) > powerOfKnight(lst,b):
        return ">"
    elif powerOfKnight(lst,a) == powerOfKnight(lst,b):
        return "="
    else:
        return "<"

inp,a = input("Enter Input : ").split("/")
inp = list(map(int,inp.split()))
print(sum(inp))
for i in a.split(","):
    i = i.split()
    print(f"{i[0]}{compareKnight(inp,int(i[0]),int(i[1]))}{i[1]}")
