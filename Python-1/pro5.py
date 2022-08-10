n=int(input("Enter Input : "))
for i in range(n+2):
    s=""
    for j in range(n-i+1):
        s+="."
    for j in range(i+1):
        s+="#"
    for j in range(n+2):
        if i==0 or i==n+1:
            s+="+"
        elif j!=0 and j!=n+1:
            s+="#"
        else:
            s+="+"
    print(s)
for i in range(n+2):
    s=""
    for j in range(n+2):
        if i==0 or i==n+1:
            s+="#"
        elif j!=0 and j!=n+1:
            s+="+"
        else:
            s+="#"
    for j in range(n-i+2):
        s+="+"
    for j in range(i):
        s+="."
    print(s)