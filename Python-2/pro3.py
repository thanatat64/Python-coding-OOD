from itertools import combinations
ans = [int(x) for x in input("Enter Your List : ").split()]
if len(ans) < 3:
    print("Array Input Length Must More Than 2")
    quit()
trueAns = []
for x in combinations(ans, 3):
    if sum(x) == 5 and sorted(x) not in trueAns:
        trueAns.append(sorted(x))

print(trueAns)
