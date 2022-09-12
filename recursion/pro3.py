def power(n,p): return 1 if p == 0 else n * power(n,p-1)
print(power(*list(map(int, input("Enter Input a b : ").split()))))
# n,p = input("Enter Input a b : ").split()
# print(power(int(n),int(p)))