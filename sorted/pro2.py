def bubble(lst):
    for _ in range(len(lst)):
        for i in range(len(lst)-1):
            swaped = False
            count = 1
            while not swaped and count + i < len(lst):
                if lst[i] > lst[i+count] and lst[i] >= 0 and lst[i+count] >= 0:
                    lst[i], lst[i+count] = lst[i+count], lst[i]  # swap this line
                    swaped = True
                else:
                    count += 1
    return lst

inp = list(map(int,input("Enter Input : ").split()))
print(*bubble(inp))