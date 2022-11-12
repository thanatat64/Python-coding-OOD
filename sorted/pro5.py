def process(lst):
    newLst = []
    newLst.append(lst[0])
    newLst.append({'points': (int(lst[1])*3) + (int(lst[3]))})
    newLst.append({'gd': int(lst[4]) - int(lst[5])})
    return newLst

def sort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if morethan(lst[j],lst[i]):
                lst[j], lst[i] = lst[i], lst[j]
    return lst

def morethan(a,b):
    if a[1]["points"] > b[1]["points"]:
        return True
    if a[1]["points"] == b[1]["points"]:
        return a[2]["gd"] > b[2]["gd"]
    return False
            

lst = input("Enter Input : ").split("/")
l,ans, = [],[]
for i in lst: 
    l.append(i.split(","))
for i in l: 
    ans.append(process(i))   
sort(ans)
print("== results ==")
print(*ans,sep ='\n')
