def bi_search(l, r, lst, data):
    mid = (l+r) // 2
    if lst[mid] == data:
        return True
    elif l == r:
        return False
    elif data < lst[mid]:
        return bi_search(l,mid-1,lst,data)
    else:
        return bi_search(mid+1,r,lst,data)
    
    
inp = input('Enter Input : ').split('/')
arr, data = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), data))