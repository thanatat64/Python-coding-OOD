def filterLess(lst,n):
    if len(lst) == 0:
        return lst
    if lst[0] < n:
        return [lst[0]] + filterLess(lst[1:],n)
    else:
        return filterLess(lst[1:],n)

def filterMore(lst, n):
    if len(lst) == 0:
        return lst
    if lst[0] >= n:
        return [lst[0]] + filterMore(lst[1:],n)
    else:
        return filterMore(lst[1:],n)

def quick_sort(l):
    return l if len(l) <= 1 else quick_sort(filterMore(l[1:],l[0])) + [l[0]] + quick_sort(filterLess(l[1:],l[0]))

lst = list(map(int,input("Enter your List : ").split(",")))
print("List after Sorted :",quick_sort(lst))
