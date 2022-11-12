def bubbleSorted(lst):
    if len(lst) <= 1:
        return lst
    if len(lst) == 2:
        return lst if lst[0] < lst[1] else [lst[1],lst[0]]
    a,b,remain,res = lst[0], lst[1], lst[2:], []
    if a < b:
        res = [a] + bubbleSorted([b] + remain)
    else:
        res = [b] + bubbleSorted([a] + remain)
    return bubbleSorted(res[:-1]) + res[-1:]

inp,lst = map(int,input("Enter Input : ").split()), []
lst.extend(inp)
print(bubbleSorted(lst))