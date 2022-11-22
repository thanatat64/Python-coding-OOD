def minimumWeight(lst,n):
    mw = 9999
    if n == 1:
        return sum(lst)
    for i in range(len(lst)):
        if len(lst[i:]) < n-1: break
        mw = min(mw,max(sum(lst[:i]),minimumWeight(lst[i:],n-1)))
    return mw
        
lst,k = input("Enter Input : ").split("/")
lst = [int(i) for i in lst.split()]
print(f"Minimum weigth for {k} box(es) = {minimumWeight(lst,int(k))}")