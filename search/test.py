def buble(L):
    step = 0
    t = []
    for last in range(len(L)-1, 0, -1):
        a = L[0]
        swap = False
        for i in range(last):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i] # swap
                swap = True
                step += 1
                t.append(f"{step} step : {L} move[{a}]")
                if last == 1:
                    t.append(f"last step : {L} move[{a}]")
        if swap is False:
            t.append(f"last step : {L} move[None]")
            break
    return t

L = list(map(int,input("Enter Input : ").split(" ")))
print('\n'.join(buble(L)))