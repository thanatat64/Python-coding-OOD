def move(n, A: list, C: list, B: list, maxN):
    if n == 0:
        return 
    if len(A) == len(B) == len(C) == 0:
        A.append('A')
        B.append('B')
        C.append('C')
        A.extend(range(n,0,-1))
        display(maxN,A,B,C)   
    move(n-1, A, B, C, maxN)
    print('move',n, 'from ', A[0], 'to', C[0])
    C.append(A.pop())
    a, b, c = A, B, C
    if b[0] == 'A':  
        a, b = b, a
    if c[0] == 'A':
        a, c = c, a
    if c[0] == 'B':
        b, c = c, b
    display(maxN,a,b,c)
    move(n-1, B, C, A, maxN)


def display(n,a,b,c):
    if n == 0:
        return
    left = '|' if len(a)-1 < n else a[n]
    mid = '|' if len(b)-1 < n else b[n]
    right = '|' if len(c)-1 < n else c[n]
    print(f"{left}  {mid}  {right}")
    display(n-1, a, b, c)


n = int(input("Enter Input : "))
move(n,[],[],[],n+1)