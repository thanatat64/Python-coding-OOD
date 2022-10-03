def asteroid_collision(asts: list,n):
    if n == len(asts)-1 or asts == []:
        return asts
    if asts[n] > 0 and asts[n+1] < 0:
        if abs(asts[n]) > abs(asts[n+1]):
            asts.pop(n+1)
        elif abs(asts[n]) < abs(asts[n+1]) :
            asts.pop(n)
        else:
            asts.pop(n+1)
            asts.pop(n)
        return asteroid_collision(asts,0)
    else:
        return asteroid_collision(asts,n+1)


x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x,0))